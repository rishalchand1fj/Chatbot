from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie
from pathlib import Path
from urllib.parse import urlparse
import json
import mimetypes
import multiprocessing as mp
import queue
import re
import time
import uuid

BASE_DIR = Path(__file__).resolve().parent
CHATBOT_DIR = BASE_DIR / "chatbots"
TEMPLATE_FILE = BASE_DIR / "templates" / "index.html"
STATIC_DIR = BASE_DIR / "static"
CHATBOT_DIR.mkdir(exist_ok=True)

workers = {}


def display_name(path: Path) -> str:
    name = path.stem
    name = re.sub(r"(?i)\b(chat\s*bot|chatbot|lab)\b", "", name)
    name = re.sub(r"[-_]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name or path.stem


def available_chatbots():
    bots = []
    for path in sorted(CHATBOT_DIR.glob("*.py"), key=lambda p: p.name.lower()):
        if path.name.startswith("_"):
            continue
        bots.append({"id": path.name, "name": display_name(path)})
    return bots


def chatbot_worker(script_path, input_queue, output_queue):
    import builtins
    import traceback

    original_input = builtins.input
    original_print = builtins.print

    def web_print(*args, sep=" ", end="\n", **kwargs):
        output_queue.put({"type": "output", "text": sep.join(str(a) for a in args) + end})

    def web_input(prompt=""):
        output_queue.put({"type": "ready", "prompt": str(prompt)})
        value = input_queue.get()
        if value is None:
            raise SystemExit
        return str(value)

    builtins.print = web_print
    builtins.input = web_input

    try:
        path = Path(script_path)
        code = path.read_text(encoding="utf-8")
        namespace = {"__name__": "__main__", "__file__": str(path)}
        exec(compile(code, str(path), "exec"), namespace, namespace)
    except SystemExit:
        pass
    except Exception:
        output_queue.put({
            "type": "error",
            "text": "The chatbot stopped because of an error:\n" + traceback.format_exc(limit=4),
        })
    finally:
        builtins.input = original_input
        builtins.print = original_print
        output_queue.put({"type": "ended"})


def stop_worker(sid):
    item = workers.pop(sid, None)
    if not item:
        return
    try:
        item["input"].put_nowait(None)
    except Exception:
        pass
    process = item.get("process")
    if process and process.is_alive():
        process.join(timeout=0.35)
        if process.is_alive():
            process.terminate()
            process.join(timeout=0.35)


def collect_output(item, max_wait=0.8):
    chunks = []
    status = "running"
    deadline = time.time() + max_wait

    while time.time() < deadline:
        try:
            msg = item["output"].get(timeout=0.05)
        except queue.Empty:
            continue

        kind = msg.get("type")
        if kind == "output":
            chunks.append(msg.get("text", ""))
        elif kind == "error":
            chunks.append(msg.get("text", ""))
            status = "ended"
            break
        elif kind == "ready":
            status = "ready"
            break
        elif kind == "ended":
            status = "ended"
            break

    return "".join(chunks).strip(), status


class Handler(BaseHTTPRequestHandler):
    server_version = "StudentChatbotPortal/1.0"

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

    def get_sid(self):
        cookie = SimpleCookie(self.headers.get("Cookie"))
        if "sid" in cookie:
            return cookie["sid"].value, False
        return str(uuid.uuid4()), True

    def send_bytes(self, data, content_type="application/octet-stream", status=200, sid=None):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        if sid:
            self.send_header("Set-Cookie", f"sid={sid}; Path=/; SameSite=Lax")
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, obj, status=200, sid=None):
        data = json.dumps(obj).encode("utf-8")
        self.send_bytes(data, "application/json; charset=utf-8", status, sid)

    def read_json(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b"{}"
            return json.loads(raw.decode("utf-8"))
        except Exception:
            return {}

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/":
            html = TEMPLATE_FILE.read_text(encoding="utf-8")
            # The page loads bot cards via /api/chatbots, so no template engine is required.
            self.send_bytes(html.encode("utf-8"), "text/html; charset=utf-8")
            return

        if path == "/api/chatbots":
            self.send_json(available_chatbots())
            return

        if path.startswith("/static/"):
            relative = path[len("/static/"):]
            file_path = (STATIC_DIR / relative).resolve()
            if file_path.parent != STATIC_DIR.resolve() or not file_path.exists() or not file_path.is_file():
                self.send_json({"error": "Not found"}, 404)
                return
            ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
            self.send_bytes(file_path.read_bytes(), ctype)
            return

        self.send_json({"error": "Not found"}, 404)

    def do_POST(self):
        path = urlparse(self.path).path
        sid, new_sid = self.get_sid()
        cookie_sid = sid if new_sid else None

        if path == "/api/start":
            data = self.read_json()
            bot_id = str(data.get("bot_id", ""))
            bot_path = (CHATBOT_DIR / bot_id).resolve()

            if bot_path.parent != CHATBOT_DIR.resolve() or not bot_path.exists() or bot_path.suffix.lower() != ".py":
                self.send_json({"error": "Chatbot not found."}, 404, cookie_sid)
                return

            stop_worker(sid)
            iq = mp.Queue()
            oq = mp.Queue()
            proc = mp.Process(target=chatbot_worker, args=(str(bot_path), iq, oq), daemon=True)
            proc.start()

            item = {"process": proc, "input": iq, "output": oq, "name": display_name(bot_path)}
            workers[sid] = item
            opening, status = collect_output(item)
            self.send_json({"name": item["name"], "message": opening, "status": status}, sid=cookie_sid)
            return

        if path == "/api/message":
            item = workers.get(sid)
            if not item:
                self.send_json({"error": "No chatbot is currently open."}, 400, cookie_sid)
                return

            if not item["process"].is_alive():
                stop_worker(sid)
                self.send_json({"message": "This chatbot has already closed.", "status": "ended"}, sid=cookie_sid)
                return

            data = self.read_json()
            text = str(data.get("message", ""))
            item["input"].put(text)
            reply, status = collect_output(item)
            if status == "ended":
                stop_worker(sid)
            self.send_json({"message": reply, "status": status}, sid=cookie_sid)
            return

        if path == "/api/close":
            stop_worker(sid)
            self.send_json({"ok": True}, sid=cookie_sid)
            return

        self.send_json({"error": "Not found"}, 404, cookie_sid)


def main():
    mp.freeze_support()
    host = "127.0.0.1"
    port = 5000
    server = ThreadingHTTPServer((host, port), Handler)
    print("=" * 58)
    print("Student Chatbot Portal")
    print(f"Open your browser at: http://{host}:{port}")
    print("Press Ctrl+C to stop the server.")
    print("=" * 58)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        for sid in list(workers):
            stop_worker(sid)
        server.server_close()


if __name__ == "__main__":
    main()

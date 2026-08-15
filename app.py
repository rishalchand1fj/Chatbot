import streamlit as st
from pathlib import Path
import builtins
import html
import re
import traceback

st.set_page_config(page_title="Student Chatbot Portal", page_icon="🤖", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
CHATBOT_DIR = BASE_DIR / "chatbots"
CHATBOT_DIR.mkdir(exist_ok=True)

# Keep the visual design of the original portal.
st.markdown(r"""
<style>
:root {
    --bg: #f4f7fb;
    --card: #ffffff;
    --text: #14213d;
    --muted: #6b7280;
    --border: #e5e7eb;
    --primary: #2563eb;
    --primary-dark: #1d4ed8;
    --danger: #dc2626;
}
.stApp { background: var(--bg); color: var(--text); }
.block-container { max-width: 1050px; padding-top: 42px; padding-bottom: 30px; }
#MainMenu, footer, header { visibility: hidden; }

.portal-header { padding: 0 4px 24px; }
.eyebrow { color: var(--primary); font-weight: 800; letter-spacing: .12em; font-size: 12px; }
.portal-header h1 { margin: 6px 0 8px; font-size: clamp(30px, 5vw, 46px); color: var(--text); }
.portal-header p, .panel-copy, .portal-footer, .status-copy { color: var(--muted); }

.portal-panel {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(20,33,61,.08);
    padding: 24px;
    margin-bottom: 0;
}
.panel-heading { display: flex; justify-content: space-between; align-items: center; gap: 20px; }
.panel-heading h2 { margin: 0 0 5px; color: var(--text); }
.panel-heading p { margin: 0; }

.bot-card-shell {
    border: 1px solid var(--border);
    background: white;
    padding: 18px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 0;
    min-height: 100px;
}
.avatar {
    width: 46px; height: 46px; border-radius: 14px;
    background: #dbeafe; color: #1d4ed8;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 20px;
}
.bot-name { font-weight: 700; font-size: 17px; color: var(--text); margin-top: 4px; }
.bot-sub { margin-top: 4px; color: var(--muted); font-size: 14px; }

/* Bot card buttons */
div[data-testid="stButton"] > button[kind="secondary"] {
    border: 1px solid var(--border);
    background: white;
    border-radius: 16px;
    font-weight: 700;
    color: var(--text);
}
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    border-color: #bfdbfe;
    color: var(--primary);
    box-shadow: 0 10px 22px rgba(37,99,235,.10);
}

.chat-panel {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(20,33,61,.08);
    overflow: hidden;
}
.chat-header-box {
    padding: 20px 22px;
    border-bottom: 1px solid var(--border);
    display:flex; align-items:center; gap:12px;
}
.chat-header-box h2 { margin:0 0 5px; font-size:18px; color:var(--text); }
.chat-header-box p { margin:0; font-size:13px; color:var(--muted); }
.online-dot { width:8px; height:8px; border-radius:50%; background:#22c55e; display:inline-block; margin-right:5px; }

.messages-box {
    min-height: 420px;
    max-height: 58vh;
    overflow-y: auto;
    padding: 24px;
    background: #f9fafb;
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
}
.message { display:flex; margin:10px 0; }
.message.user { justify-content:flex-end; }
.message.bot, .message.system { justify-content:flex-start; }
.bubble { max-width:min(76%,680px); padding:12px 15px; border-radius:15px; line-height:1.45; white-space:pre-wrap; overflow-wrap:anywhere; }
.message.user .bubble { background:var(--primary); color:white; border-bottom-right-radius:4px; }
.message.bot .bubble { background:white; border:1px solid var(--border); color:var(--text); border-bottom-left-radius:4px; }
.message.system .bubble { background:#fff7ed; border:1px solid #fed7aa; color:#9a3412; font-size:13px; }

.portal-footer { text-align:center; font-size:13px; padding:22px 0 10px; }
.portal-footer code, .panel-copy code { background:#f1f5f9; padding:2px 5px; border-radius:5px; }

/* Text input styled like the original composer */
div[data-testid="stTextInput"] input {
    padding: 12px 14px;
    border: 1px solid #d1d5db;
    border-radius: 11px;
}
div[data-testid="stTextInput"] input:focus {
    border-color:#93c5fd;
    box-shadow:0 0 0 3px #dbeafe;
}

@media (max-width:650px) {
    .block-container { padding-top:28px; }
    .portal-panel { padding:17px; }
    .bubble { max-width:88%; }
    .messages-box { min-height:360px; }
}
</style>
""", unsafe_allow_html=True)


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
        bots.append({"id": path.name, "name": display_name(path), "path": path})
    return bots


class AwaitingInput(Exception):
    pass


def run_student_chatbot(script_path: Path, supplied_messages):
    """Replay supplied inputs through an unchanged input()/print() student chatbot.
    Returns only output produced after the newest supplied input. With no supplied
    inputs, returns the opening text printed before the first input().
    """
    outputs = []
    values = iter(supplied_messages)
    total = len(supplied_messages)
    consumed = 0
    capture = total == 0

    original_input = builtins.input
    original_print = builtins.print

    def web_print(*args, sep=" ", end="\n", **kwargs):
        if capture:
            outputs.append(sep.join(str(a) for a in args) + end)

    def web_input(prompt=""):
        nonlocal consumed, capture
        try:
            value = next(values)
        except StopIteration:
            raise AwaitingInput()
        consumed += 1
        if consumed == total:
            capture = True
        return str(value)

    builtins.input = web_input
    builtins.print = web_print
    ended = False
    error = None

    try:
        code = script_path.read_text(encoding="utf-8")
        namespace = {"__name__": "__main__", "__file__": str(script_path)}
        exec(compile(code, str(script_path), "exec"), namespace, namespace)
        ended = True
    except AwaitingInput:
        ended = False
    except SystemExit:
        ended = True
    except Exception:
        error = traceback.format_exc(limit=5)
        ended = True
    finally:
        builtins.input = original_input
        builtins.print = original_print

    return "".join(outputs).strip(), ended, error


def init_state():
    defaults = {
        "selected_bot": None,
        "selected_bot_name": None,
        "messages": [],
        "user_inputs": [],
        "bot_ended": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def open_bot(bot):
    st.session_state.selected_bot = bot["id"]
    st.session_state.selected_bot_name = bot["name"]
    st.session_state.messages = []
    st.session_state.user_inputs = []
    st.session_state.bot_ended = False

    opening, ended, error = run_student_chatbot(bot["path"], [])
    if opening:
        st.session_state.messages.append({"role": "bot", "content": opening})
    if error:
        st.session_state.messages.append({"role": "system", "content": "The chatbot stopped because of an error:\n" + error})
        ended = True
    st.session_state.bot_ended = ended


def close_bot():
    st.session_state.selected_bot = None
    st.session_state.selected_bot_name = None
    st.session_state.messages = []
    st.session_state.user_inputs = []
    st.session_state.bot_ended = False


def render_message(message):
    role = message.get("role", "bot")
    css_role = "user" if role == "user" else ("system" if role == "system" else "bot")
    content = html.escape(str(message.get("content", "")))
    st.markdown(
        f'<div class="message {css_role}"><div class="bubble">{content}</div></div>',
        unsafe_allow_html=True,
    )


init_state()
bots = available_chatbots()

# Header from the original interface.
st.markdown("""
<div class="portal-header">
    <div class="eyebrow">ITC245</div>
    <h1>Student Chatbot Portal</h1>
    <p>Select a student's chatbot and start chatting.</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.selected_bot is None:
    st.markdown("""
    <div class="portal-panel">
        <div class="panel-heading">
            <div>
                <h2>Choose a chatbot</h2>
                <p class="panel-copy">Any <code>.py</code> file placed in the <code>chatbots</code> folder appears here automatically.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    refresh_col, _ = st.columns([1.3, 5])
    with refresh_col:
        if st.button("Refresh list", use_container_width=True):
            st.rerun()

    if not bots:
        st.warning("No chatbot files found. Add a Python file to the chatbots folder.")
    else:
        # Two-column grid, matching the original responsive card layout.
        for start in range(0, len(bots), 2):
            cols = st.columns(2)
            for offset in range(2):
                i = start + offset
                if i >= len(bots):
                    continue
                bot = bots[i]
                with cols[offset]:
                    initial = html.escape(bot["name"][:1].upper())
                    safe_name = html.escape(bot["name"])
                    st.markdown(
                        f"""
                        <div class="bot-card-shell">
                            <div class="avatar">{initial}</div>
                            <div>
                                <div class="bot-name">{safe_name}</div>
                                <div class="bot-sub">Open chatbot</div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    if st.button(f"Open {bot['name']}", key=f"open_{bot['id']}", use_container_width=True):
                        open_bot(bot)
                        st.rerun()

    st.markdown(
        '<div class="portal-footer">To add another student, place their Python chatbot file inside <code>chatbots/</code>, then click <strong>Refresh list</strong>.</div>',
        unsafe_allow_html=True,
    )

else:
    selected = next((b for b in bots if b["id"] == st.session_state.selected_bot), None)

    if selected is None:
        st.error("This chatbot file could not be found.")
        if st.button("Close Chat"):
            close_bot()
            st.rerun()
    else:
        header_left, header_right = st.columns([5, 1.35])
        with header_left:
            initial = html.escape(selected["name"][:1].upper())
            safe_name = html.escape(selected["name"])
            status = "Closed" if st.session_state.bot_ended else "Running"
            st.markdown(
                f"""
                <div class="chat-panel">
                    <div class="chat-header-box">
                        <div class="avatar">{initial}</div>
                        <div>
                            <h2>{safe_name}</h2>
                            <p><span class="online-dot"></span> {status}</p>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with header_right:
            if st.button("Close Chat", type="secondary", use_container_width=True):
                close_bot()
                st.rerun()

        st.markdown('<div class="messages-box">', unsafe_allow_html=True)
        for message in st.session_state.messages:
            render_message(message)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.bot_ended:
            st.info("The chatbot has closed. Use Close Chat to return to the selection screen.")
        else:
            with st.form("chat_form", clear_on_submit=True):
                text_col, send_col = st.columns([7, 1.25])
                with text_col:
                    message = st.text_input("Message", placeholder="Type your message...", label_visibility="collapsed")
                with send_col:
                    submitted = st.form_submit_button("Send", type="primary", use_container_width=True)

            if submitted and message.strip():
                text = message.strip()
                st.session_state.messages.append({"role": "user", "content": text})
                st.session_state.user_inputs.append(text)

                reply, ended, error = run_student_chatbot(selected["path"], st.session_state.user_inputs)
                if error:
                    st.session_state.messages.append({"role": "system", "content": "The chatbot stopped because of an error:\n" + error})
                    st.session_state.bot_ended = True
                else:
                    if reply:
                        st.session_state.messages.append({"role": "bot", "content": reply})
                    else:
                        st.session_state.messages.append({"role": "bot", "content": "(No text response)"})
                    st.session_state.bot_ended = ended
                st.rerun()

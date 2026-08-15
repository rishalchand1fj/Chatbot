import streamlit as st
from pathlib import Path
import builtins
import re
import traceback

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="ITC245 Student Chatbot Portal",
    page_icon="🤖",
    layout="centered"
)

# ---------------------------------------------------------
# FOLDER SETTINGS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
CHATBOT_DIR = BASE_DIR / "chatbots"

# Create folder if it does not exist
CHATBOT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .bot-header {
        text-align: center;
        padding: 15px;
        border-radius: 12px;
        background-color: rgba(128,128,128,0.08);
        margin-bottom: 20px;
    }

    .bot-count {
        text-align: center;
        font-size: 14px;
        color: #777;
        margin-bottom: 20px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        min-height: 50px;
        font-size: 16px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HELPER: CLEAN STUDENT NAME
# ---------------------------------------------------------

def display_name(path: Path) -> str:
    """
    Convert file names such as:

    ChatBot - Nelson Marsh.py
    Lab chatbot - Rohan Ravinesh Prasad.py

    into:

    Nelson Marsh
    Rohan Ravinesh Prasad
    """

    name = path.stem

    # Remove common words
    name = re.sub(
        r"(?i)\\b(chat\\s*bot|chatbot|lab)\\b",
        "",
        name
    )

    # Replace dashes and underscores with spaces
    name = re.sub(r"[-_]+", " ", name)

    # Remove repeated spaces
    name = re.sub(r"\\s+", " ", name).strip()

    return name or path.stem


# ---------------------------------------------------------
# FIND ALL CHATBOTS
# ---------------------------------------------------------

def available_chatbots():

    bots = []

    for path in sorted(
        CHATBOT_DIR.glob("*.py"),
        key=lambda p: p.name.lower()
    ):

        # Ignore files starting with _
        if path.name.startswith("_"):
            continue

        bots.append(
            {
                "id": path.name,
                "name": display_name(path),
                "path": path
            }
        )

    return bots


# ---------------------------------------------------------
# SPECIAL EXCEPTION
# ---------------------------------------------------------

class AwaitingInput(Exception):
    """
    Used internally when the student's chatbot reaches input()
    and is waiting for another question.
    """
    pass


# ---------------------------------------------------------
# RUN STUDENT CHATBOT
# ---------------------------------------------------------

def run_student_chatbot(
    script_path: Path,
    previous_inputs,
    capture_opening=False
):

    """
    Runs a student's original console chatbot.

    The student's code can continue using:

        input()
        print()

    No modification to the student's chatbot is required.

    Streamlit replays previous questions through the chatbot
    and captures the response to the newest question.
    """

    outputs = []

    # Make an iterator containing all previous user questions
    supplied_inputs = iter(previous_inputs)

    number_of_inputs = len(previous_inputs)

    consumed_inputs = 0

    # Opening screen should capture text printed before first input()
    capture_output = capture_opening or number_of_inputs == 0

    # Save original Python functions
    original_input = builtins.input
    original_print = builtins.print


    # -----------------------------------------------------
    # REPLACE print()
    # -----------------------------------------------------

    def browser_print(
        *args,
        sep=" ",
        end="\\n",
        **kwargs
    ):

        nonlocal capture_output

        if capture_output:

            text = sep.join(
                str(item)
                for item in args
            )

            outputs.append(text + end)


    # -----------------------------------------------------
    # REPLACE input()
    # -----------------------------------------------------

    def browser_input(prompt=""):

        nonlocal capture_output
        nonlocal consumed_inputs

        try:

            value = next(supplied_inputs)

        except StopIteration:

            # Student chatbot has reached the next input()
            # and is waiting for the user.
            raise AwaitingInput()

        consumed_inputs += 1

        # When the newest question is supplied,
        # begin recording the chatbot's response.
        if consumed_inputs == number_of_inputs:

            capture_output = True

        return str(value)


    # -----------------------------------------------------
    # APPLY REPLACEMENTS
    # -----------------------------------------------------

    builtins.input = browser_input
    builtins.print = browser_print

    ended = False
    error = None


    try:

        # Read student's Python program
        code = script_path.read_text(
            encoding="utf-8"
        )

        # Give the student's program its own namespace
        namespace = {
            "__name__": "__main__",
            "__file__": str(script_path)
        }

        # Execute student's original program
        exec(
            compile(
                code,
                str(script_path),
                "exec"
            ),
            namespace,
            namespace
        )

        # If program finishes normally
        ended = True


    except AwaitingInput:

        # This is normal.
        # It means chatbot is waiting for next message.
        ended = False


    except SystemExit:

        ended = True


    except Exception:

        error = traceback.format_exc(limit=5)
        ended = True


    finally:

        # Restore normal Python functions
        builtins.input = original_input
        builtins.print = original_print


    result = "".join(outputs).strip()

    return result, ended, error


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "selected_bot" not in st.session_state:
    st.session_state.selected_bot = None

if "selected_bot_name" not in st.session_state:
    st.session_state.selected_bot_name = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_inputs" not in st.session_state:
    st.session_state.user_inputs = []

if "bot_ended" not in st.session_state:
    st.session_state.bot_ended = False


# ---------------------------------------------------------
# OPEN CHATBOT
# ---------------------------------------------------------

def open_chatbot(bot):

    st.session_state.selected_bot = bot["id"]
    st.session_state.selected_bot_name = bot["name"]

    st.session_state.messages = []
    st.session_state.user_inputs = []
    st.session_state.bot_ended = False

    # Capture chatbot opening message
    opening, ended, error = run_student_chatbot(
        bot["path"],
        [],
        capture_opening=True
    )

    if opening:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": opening
            }
        )

    if error:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content":
                    "⚠️ This student's chatbot contains an error:\\n\\n"
                    + error
            }
        )

        st.session_state.bot_ended = True

    elif ended:

        st.session_state.bot_ended = True


# ---------------------------------------------------------
# CLOSE CHATBOT
# ---------------------------------------------------------

def close_chatbot():

    st.session_state.selected_bot = None
    st.session_state.selected_bot_name = None
    st.session_state.messages = []
    st.session_state.user_inputs = []
    st.session_state.bot_ended = False


# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.selected_bot is None:

    st.markdown(
        '<div class="main-title">🤖 ITC245 Student Chatbots</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Select a student chatbot to begin chatting'
        '</div>',
        unsafe_allow_html=True
    )

    bots = available_chatbots()

    if len(bots) == 0:

        st.warning(
            "No student chatbots were found."
        )

        st.info(
            "Place Python chatbot files inside the "
            "`chatbots` folder."
        )

        st.code(
            """
chatbots/
    Nelson Marsh.py
    Rohan Ravinesh Prasad.py
    Tom.py
            """,
            language="text"
        )

    else:

        st.markdown(
            f'<div class="bot-count">'
            f'{len(bots)} chatbot(s) available'
            f'</div>',
            unsafe_allow_html=True
        )

        # -------------------------------------------------
        # DISPLAY STUDENT CHATBOTS
        # -------------------------------------------------

        for index, bot in enumerate(bots):

            col1, col2 = st.columns(
                [1, 5]
            )

            with col1:

                st.markdown(
                    "<h2 style='text-align:center;'>🤖</h2>",
                    unsafe_allow_html=True
                )

            with col2:

                if st.button(
                    f"Chat with {bot['name']}",
                    key=f"bot_{index}_{bot['id']}",
                    use_container_width=True
                ):

                    open_chatbot(bot)

                    st.rerun()


        st.divider()

        if st.button(
            "🔄 Refresh Chatbot List",
            use_container_width=True
        ):

            st.rerun()


        st.caption(
            "To add another student, place their `.py` "
            "chatbot file inside the `chatbots` folder."
        )


# =========================================================
# CHAT PAGE
# =========================================================

else:

    bots = available_chatbots()

    selected = next(
        (
            bot
            for bot in bots
            if bot["id"] == st.session_state.selected_bot
        ),
        None
    )


    # -----------------------------------------------------
    # CHATBOT FILE WAS DELETED
    # -----------------------------------------------------

    if selected is None:

        st.error(
            "This chatbot file could not be found."
        )

        if st.button("⬅️ Return to Chatbots"):

            close_chatbot()

            st.rerun()


    else:

        # -------------------------------------------------
        # HEADER
        # -------------------------------------------------

        top_left, top_right = st.columns(
            [3, 1]
        )

        with top_left:

            st.markdown(
                f"""
                <div class="bot-header">
                    <h2>🤖 {selected["name"]}</h2>
                    <p>Student Chatbot</p>
                </div>
                """,
                unsafe_allow_html=True
            )


        with top_right:

            if st.button(
                "❌ Close Chat",
                use_container_width=True
            ):

                close_chatbot()

                st.rerun()


        # -------------------------------------------------
        # DISPLAY CHAT HISTORY
        # -------------------------------------------------

        for message in st.session_state.messages:

            with st.chat_message(
                message["role"]
            ):

                st.text(
                    message["content"]
                )


        # -------------------------------------------------
        # CHAT INPUT
        # -------------------------------------------------

        if not st.session_state.bot_ended:

            question = st.chat_input(
                f"Ask {selected['name']}'s chatbot a question..."
            )


            if question:

                # Store user message
                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": question
                    }
                )

                # Store question for replay
                st.session_state.user_inputs.append(
                    question
                )


                # -----------------------------------------
                # RUN STUDENT CHATBOT
                # -----------------------------------------

                response, ended, error = run_student_chatbot(
                    selected["path"],
                    st.session_state.user_inputs
                )


                # -----------------------------------------
                # HANDLE ERROR
                # -----------------------------------------

                if error:

                    response = (
                        "⚠️ The student's chatbot encountered "
                        "an error:\\n\\n"
                        + error
                    )

                    ended = True


                # -----------------------------------------
                # EMPTY RESPONSE
                # -----------------------------------------

                if not response:

                    response = (
                        "The chatbot did not return a response."
                    )


                # -----------------------------------------
                # STORE BOT RESPONSE
                # -----------------------------------------

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )


                st.session_state.bot_ended = ended

                st.rerun()


        # -------------------------------------------------
        # CHATBOT CLOSED
        # -------------------------------------------------

        else:

            st.info(
                "This chatbot has finished running."
            )

            if st.button(
                "⬅️ Return to Student Chatbots",
                use_container_width=True
            ):

                close_chatbot()

                st.rerun()

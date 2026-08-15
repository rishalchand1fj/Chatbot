STUDENT CHATBOT PORTAL
======================

PURPOSE
-------
This browser interface automatically lists every Python (.py) chatbot placed inside the "chatbots" folder.
The students' original chatbot files can continue using normal input() and print() statements.

CURRENT CHATBOTS
----------------
- Nelson Marsh.py
- Rohan Ravinesh Prasad.py

HOW TO RUN ON WINDOWS
---------------------
1. Make sure Python 3 is installed.
2. Extract this whole folder somewhere on your computer.
3. Open Command Prompt in the "student_chatbot_portal" folder.
4. Run:

   python app.py

5. You will see:

   Open your browser at: http://127.0.0.1:5000

6. Open that address in Chrome, Edge, Firefox, etc.

No pip install is required.

HOW TO ADD ANOTHER STUDENT, FOR EXAMPLE TOM
-------------------------------------------
1. Copy Tom's Python chatbot file into:

   student_chatbot_portal/chatbots/

   Example:
   student_chatbot_portal/chatbots/Tom.py

2. Do NOT edit app.py.
3. In the browser click "Refresh list".
4. Tom will automatically appear as a third option.

The same applies to a fourth, fifth, or later student.

HOW IT WORKS
------------
- Home page: choose Nelson, Rohan, Tom, etc.
- The chosen Python program starts in a separate worker process.
- The webpage sends your typed message to the program's normal input().
- The program's print() output appears as the chatbot reply.
- Click "Close Chat" to stop that chatbot and return to the selection page.
- You can then open another student's chatbot.

IMPORTANT COMPATIBILITY NOTE
----------------------------
This automatic launcher is designed for simple console chatbots that use input() and print(), like the two supplied examples.
A student file that uses Tkinter, external APIs, databases, special packages, or reads extra files may need additional setup.

TO STOP THE WEBSITE
-------------------
Go back to Command Prompt and press Ctrl+C.

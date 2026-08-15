# itc245_chatbot.py
# ITC245 Course FAQ Chatbot – Rule‑based with if/elif/else

print("=" * 50)
print(" ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to close the chatbot.")
print("Type 'help' to view available questions.\n")

while True:
    question = input("You: ").strip()
    q = question.lower()

    if q == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    if q == "":
        print("Assistant: Please enter a question.\n")
        continue

    # ----- Help -----
    if q == "help":
        print("\nYou can ask questions about:")
        print("- Course code")
        print("- Course title")
        print("- Semester")
        print("- Lecturer")
        print("- Class time")
        print("- Classroom / venue")
        print("- Course duration")
        print("- Assessments")
        print("- Assignments")
        print("- Laboratory activities")
        print("- Attendance")
        print("- Moodle")
        print("- Required software")
        print("- Submission process")
        print("- Final examination")
        print("- Student consultation")
        print("- Late submission")
        print("- Use of Artificial Intelligence\n")
        continue

    # ----- Greetings -----
    if "hello" in q or "hi" in q or "hey" in q:
        print("ITC245 Bot: Hello! Welcome to ITC245. How can I help you?\n")
        continue

    # ----- Course code -----
    if "course code" in q or "code" in q:
        print("ITC245 Bot: The course code is ITC245 – Introduction to Programming.\n")
        continue

    # ----- Course title -----
    if "course title" in q or "title" in q or "name of the course" in q:
        print("ITC245 Bot: The course title is 'Introduction to Programming'.\n")
        continue

    # ----- Semester -----
    if "semester" in q:
        print("ITC245 Bot: The course is offered in Semester 1, 2026 (February – June).\n")
        continue

    # ----- Lecturer -----
    if "lecturer" in q or "instructor" in q or "teacher" in q:
        print("ITC245 Bot: The lecturer is Mr Rishal Chand.\n")
        continue

    # ----- Class time -----
    if "class time" in q or "schedule" in q or "when is the class" in q:
        print("ITC245 Bot: Classes are held on Tuesdays 09:00–11:00 and Wednesdays 11:00–13:00.\n")
        continue

    # ----- Classroom / venue -----
    if "classroom" in q or "venue" in q or "room" in q or "where" in q:
        print("ITC245 Bot: Classes are held in Building B, Room 105.\n")
        continue

    # ----- Course duration -----
    if "duration" in q or "how long" in q or "weeks" in q:
        print("ITC245 Bot: The course runs for 12 weeks (july to november).\n")
        continue

    # ----- Assessments -----
    if "assessment" in q or "grading" in q:
        print("ITC245 Bot: Assessments consist of:\n"
              "  • Assignment 1 – 20%\n"
              "  • Assignment 2 – 30%\n"
              "  • Final Examination – 50%\n")
        continue

    # ----- Assignments -----
    if "assignment" in q or "project" in q:
        print("ITC245 Bot: There are two programming assignments:\n"
              "  • Assignment 1 (20%) – due Week 5\n"
              "  • Assignment 2 (30%) – due Week 10\n")
        continue

    # ----- Laboratory activities -----
    if "lab" in q or "laboratory" in q or "practical" in q:
        print("ITC245 Bot: Weekly laboratory sessions are held in the computer labs. "
              "Attendance is strongly encouraged to complete practical exercises.\n")
        continue

    # ----- Attendance -----
    if "attendance" in q or "attend" in q:
        print("ITC245 Bot: 80% attendance is required to pass the course. "
              "Notify your lecturer if you are unable to attend.\n")
        continue

    # ----- Moodle -----
    if "moodle" in q or "lms" in q:
        print("ITC245 Bot: All materials, announcements, and submissions are available on Moodle. "
              "Check it regularly.\n")
        continue

    # ----- Required software -----
    if "software" in q or "tools" in q or "what do i need" in q:
        print("ITC245 Bot: You will need:\n"
              "  • Python 3.x (latest version recommended)\n"
              "  • Visual Studio Code (with Python extension)\n"
              "  • A modern web browser for Moodle\n")
        continue

    # ----- Submission process -----
    if "submission" in q or "submit" in q or "hand in" in q:
        print("ITC245 Bot: Assignments are submitted via the Moodle submission portal. "
              "Ensure you submit before the deadline.\n")
        continue

    # ----- Final examination -----
    if "final exam" in q or "examination" in q or "exam" in q:
        print("ITC245 Bot: The 3‑hour final examination will be held during the official exam period. "
              "Details will be announced on Moodle.\n")
        continue

    # ----- Student consultation -----
    if "consultation" in q or "office hours" in q or "appointment" in q:
        print("ITC245 Bot: Student consultation is available Wednesdays 16:00–17:00 "
              "or by appointment. Email the lecturer to book.\n")
        continue

    # ----- Late submission -----
    if "late submission" in q or "late" in q or "penalty" in q:
        print("ITC245 Bot: Late submissions incur a 10% deduction per day (including weekends). "
              "Extensions must be requested before the deadline.\n")
        continue

    # ----- Use of Artificial Intelligence -----
    if "artificial intelligence" in q or "ai" in q or "chatgpt" in q:
        print("ITC245 Bot: The use of AI tools (e.g., ChatGPT) is permitted provided you "
              "clearly attribute any AI‑generated content. Misuse is academic misconduct.\n")
        continue

    # ----- Fallback -----
    print("ITC245 Bot: Sorry, I do not know the answer to that. "
          "Type 'help' to see the topics I can handle.\n")
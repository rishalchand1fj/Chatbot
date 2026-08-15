print ("=" * 50)
print ("Welcome to ITC245  Chatbot")

while True:
    question = input ("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("Jarvis: Goodbye! Have a nice time.")
        break

    if question == "":
        print("Jarvis: Please enter a question.\n")
        continue

    if "hello" in question_lower or "hi" in question_lower or "hey" in question_lower:
        print("Jarvis: Helloo! Welcome to ITC245.")

    elif "course code" in question_lower or "code" in question_lower:
        print("Jarvis: Course Code is ITC245.")
    
    elif "course title" in question_lower or "title" in question_lower:
        print("Jarvis: Course Title is Artificial Intelligence Techniques.")

    elif "semester" in question_lower:
        print("Jarvis: ITC245 is offered in Semester 2, 2026.")

    elif "lecturer" in question_lower:
        print("Jarvis: The lecturer is Mr Rishal Chand.")

    elif "class time" in question_lower or "time" in question_lower:
        print("Jarvis: Lecture:Tuesday from 9.00 AM to 11.00 AM in B105.\n" \
        "Tutorial:Monday from 3.00 PM to 4.00 PM in B104. " \
        "\nLab:Wednesday from 11.00 AM to 1.00 PM in C100")

    elif "classroom" in question_lower or "venue" in question_lower:
        print("Jarvis: Lecture is in B105\nTutorial is in B104\nLab is in C100")

    elif "duration" in question_lower:
        print("Jarvis: This course is provided in Semester 2, 2026")

    elif "assessment" in question_lower:
        print("Jarvis: Includes assignments, labs, and exam")

    elif "assignment" in question_lower:
        print("Jarvis: There is no assignment in ITC245.")

    elif "lab activities" in question_lower or "laboratory activities" in question_lower:
        print("Jarvis: Once a week lab session." \
        "In class activities or submission" \
        "Wednesdays 11am - 1pm Room-C100")

    elif "attendance" in question_lower:
        print("Jarvis: Attendance is mandotary")
    elif "moodle" in question_lower:
        print("Jarvis: Use Moodle to upload materials")
    elif "required software" in question_lower or "software" in question_lower:
        print("Jarvis: Use VS Code with Python extensions")
    elif "submission process" in question_lower or "submission" in question_lower:
        print("Jarvis: Submit via Moodle and Tophat")
    elif "final examination" in question_lower or "final exam" in question_lower or "final" in question_lower:
        print("Jarvis: Final exam at end of semester\nShort test in week 7")
    elif "student consultation" in question_lower or "consult" in question_lower:
        print("Jarvis: Contact lecturer during office hours")
    elif "late" in question_lower:
        print("Jarvis: Late submissions may get penalties and points deducted")
    elif "Artificial Intelligence" in question_lower or "ai" in question_lower:
        print("Jarvis: AI use must follow university rules")
    else:
        print("Jarvis: SORRY!! I do not know the answer")

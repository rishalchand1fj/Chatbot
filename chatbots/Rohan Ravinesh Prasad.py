print("=" * 50)
print("        ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to close the chatbot \n.")
print("Type 'help' to review all the available questions.")

while True:
    question= input("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    if question == "":
        print("Assistant: Please enter a question \n.")
        continue

    if "hello" in question_lower or "hi" in question_lower:
        print("ITC245 BOT: HELLO! Welcome to ITC245.")

    elif "help" in question_lower:
        print("n\ You can ask questions about:")
        print("-Course code")
        print("- Semester")
        print("- Lecturer")
        print("- Class time")
        print("- Classroom or venue")
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
        print("- Use of Artificial Intelligence")

    elif "code" in question_lower:
        print("ITC245 BOT: The course code is ITC245.")

    elif "title" in question_lower or "name of course" in question_lower:
        print("ITC245 BOT: The course title is Artificial Intellgence Techniques.")

    elif "semester" in question_lower:
        print("ITC245 BOT: This course is offered in Semester 2, 2026.")

    elif "lecturer" in question_lower or "teacher" in question_lower or "instructor" in question_lower:
        print("ITC245 BOT: The course lecturer is Mr.Rishal.")

    elif "time" in question_lower or "when is class" in question_lower:
        print("ITC245 BOT: Classes are held on Mondays and Wednesdays from 9:00 AM to 1:00 PM.")

    elif "room" in question_lower or "venue" in question_lower or "location" in question_lower or "where" in question_lower:
        print("ITC245 BOT: The class venue is Lab C100.")

    elif "duration" in question_lower or "how long" in question_lower:
        print("ITC245 BOT: The course duration is 14 weeks.")

    elif "assessment" in question_lower or "mark" in question_lower or "grade" in question_lower:
        print("ITC245 BOT: Assessments consist of Assignments (30%), Labs (20%), Midterm (10%), and Final Exam (40%).")

    elif "assignment" in question_lower:
        print("ITC245 BOT: There are one major assignments due in time given by the lecturer.")

    elif "lab" in question_lower or "laboratory" in question_lower:
        print("ITC245 BOT: Weekly laboratory activities are conducted every Wednesdy.")

    elif "attendance" in question_lower:
        print("ITC245 BOT: A minimum of 80% attendance in lectures and labs is required to pass.")

    elif "moodle" in question_lower:
        print("ITC245 BOT: All course announcements and resources are available on Moodle.")

    elif "software" in question_lower or "program" in question_lower or "tool" in question_lower:
        print("ITC245 BOT: The required software includes Python 3.x, MySQL, and Visual Studio Code.")

    elif "submission" in question_lower or "submit" in question_lower:
        print("ITC245 BOT: Submit all assignments online through the Moodle submission portal.")

    elif "exam" in question_lower or "examination" in question_lower or "final" in question_lower:
        print("ITC245 BOT: The final examination will take place during the university exam period.")

    elif "consultation" in question_lower or "office hour" in question_lower:
        print("ITC245 BOT: Student consultation hours are Tuesdays and Thursdays from 2:00 PM to 4:00 PM.")

    elif "late" in question_lower or "penalty" in question_lower:
        print("ITC245 BOT: Late submissions wiil give mark redution penalty.")

    elif "ai" in question_lower or "artificial intelligence" in question_lower or "chatgpt" in question_lower:
        print("ITC245 BOT: Generative AI tools may be used for assistance, but all submitted work must be original.")

    else:
        print("ITC245 BOT: Sorry, I don't understand that question. Type 'help' to see what you can ask.")

    print()
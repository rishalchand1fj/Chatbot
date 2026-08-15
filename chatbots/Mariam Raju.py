print("=" * 50)
print("         ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to close the chatbot.\n")
print("Type 'help' to view available questions.\n")

while True:
    question = input("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    if question == "":
        print("Assistant: Please enter a question.\n")
        continue

    if "hello" in question_lower or "hi" in question_lower:
        print("Assistant: Hello! Welcome to ITC245.")

    elif "help" in question_lower:
        print("\nYou can ask questions about:")
        print("- Course code")
        print("- Course title")
        print("- Semester")
        print("- Lecturer")
        print("- Class time")
        print("- Classroom")
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
        print("- Artificial Intelligence")

    elif "course code" in question_lower or "code" in question_lower:
        print("Assistant: The course code is ITC245.")

    elif "course title" in question_lower or "title" in question_lower:
        print("Assistant: The course title is Artifical Intelligence Techniques .")

    elif "semester" in question_lower:
        print("Assistant: The course is offered in Semester 2, 2026.")

    elif "lecturer" in question_lower:
        print("Assistant: Your lecturer is Rishal Chand.")

    elif "class time" in question_lower or "time" in question_lower:
        print("Assistant: Classes are held at 11am to 1pm.")

    elif "classroom" in question_lower or "venue" in question_lower or "room" in question_lower:
        print("Assistant: The classroom is in c001.")

    elif "duration" in question_lower:
        print("Assistant: The course duration is one semester.")

    elif "assessment" in question_lower:
        print("Assistant: Assessments include labs, assignments, quizzes and the final examination.")

    elif "assignment" in question_lower:
        print("Assistant: Assignment details are available on Tophat.")

    elif "lab" in question_lower or "laboratory" in question_lower:
        print("Assistant: Laboratory activities are conducted during your scheduled lab sessions.")

    elif "attendance" in question_lower:
        print("Assistant:Students are required to attend 2hrs of lectuer 2 hrs of lab and 1hr oh tutorial.")

    elif "moodle" in question_lower:
        print("Assistant: Course materials and announcements are available on Moodle.")

    elif "software" in question_lower:
        print("Assistant: Required software includes Visual Studio Code and Python.")

    elif "submission" in question_lower:
        print("Assistant: Submit your assignments through Tophat oe moodle.")

    elif "exam" in question_lower or "final examination" in question_lower:
        print("Assistant: The final examination will be held during the official examination period.")

    elif "consultation" in question_lower:
        print("Assistant: Please contact your lecturer during consultation hours or by appointment.")

    elif "late" in question_lower:
        print("Assistant: Late submissions may receive penalties according to the course policy.")

    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("Assistant: Artificial Intelligence may only be used according to the course guidelines.")

    else:
        print("Assistant: Sorry, I do not know the answer.")

    print()

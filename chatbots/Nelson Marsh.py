print("=" * 50)
print("ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to close the chatbot.")
print("Type 'help' to view available questions.")

while True:
    question = input("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    elif question == "":
        print("Assistant: Please enter a question.")

    elif "hello" in question_lower or "hi" in question_lower:
        print("ITC245 Bot: Hello! Welcome to ITC245.")

    elif "help" in question_lower:
        print("\nYou can ask questions about:")
        print("- Course code")
        print("- Course title")
        print("- Semester")
        print("- Lecturer")
        print("- Class Time")
        print("- Classroom or Venue")
        print("- Course Duration")
        print("- Assessment")
        print("- Assignments")
        print("- Laboratory Activities")
        print("- Attendance")
        print("- Moodle")
        print("- Required Software")
        print("- Submission Process")
        print("- Final Examination")
        print("- Student Consultation")
        print("- Late Submission")
        print("- Use of Artificial Intelligence")

    elif "code" in question_lower:
        print("ITC245 Bot: The course code is ITC245.")

    elif "title" in question_lower or "name" in question_lower:
        print("ITC245 Bot: The course title is AI Techniques.")

    elif "semester" in question_lower:
        print("ITC245 Bot: This course is offered in Semester 1, 2026.")

    elif "lecturer" in question_lower or "teacher" in question_lower or "who teaches" in question_lower:
        print("ITC245 Bot: The lecturer for ITC245 is Mr. Jashnil Kumar.")

    elif "time" in question_lower or "when" in question_lower:
        print("ITC245 Bot: Please check your Semester 1 timetable on the student portal for the exact class time.")

    elif "venue" in question_lower or "classroom" in question_lower or "room" in question_lower or "where" in question_lower:
        print("ITC245 Bot: Please check your timetable for the classroom/venue for ITC245.")

    elif "duration" in question_lower or "how long" in question_lower:
        print("ITC245 Bot: ITC245 runs for the full semester (Semester 1, 2026).")

    elif "assessment" in question_lower or "grading" in question_lower or "marks" in question_lower:
        print("ITC245 Bot: Assessment usually includes labs, tests, assignments and a final exam. Check Moodle for the exact breakdown.")

    elif "assignment" in question_lower:
        print("ITC245 Bot: Assignments are posted on Moodle. Check the course page for due dates.")

    elif "lab" in question_lower or "laboratory" in question_lower:
        print("ITC245 Bot: Laboratory activities are done weekly and cover practical AI techniques exercises.")

    elif "attendance" in question_lower:
        print("ITC245 Bot: Attendance is compulsory for all lectures and labs.")

    elif "moodle" in question_lower:
        print("ITC245 Bot: Moodle is used to post course materials, assignments and announcements.")

    elif "software" in question_lower or "install" in question_lower:
        print("ITC245 Bot: You will need Python and Visual Studio Code installed for this course.")

    elif "submit" in question_lower or "submission" in question_lower:
        print("ITC245 Bot: Assignments must be submitted through Moodle before the deadline.")

    elif "exam" in question_lower:
        print("ITC245 Bot: The final examination covers all topics taught during the semester.")

    elif "consultation" in question_lower or "consult" in question_lower:
        print("ITC245 Bot: Student consultation hours are available. Please check with your lecturer for the schedule.")

    elif "late" in question_lower:
        print("ITC245 Bot: Late submissions may be penalized according to the university policy.")

    elif "ai" in question_lower or "artificial intelligence" in question_lower:
        print("ITC245 Bot: Use of AI tools must follow the university's academic integrity guidelines.")

    else:
        print("ITC245 Bot: Sorry, I don't understand that question. Type 'help' to see what I can answer.")
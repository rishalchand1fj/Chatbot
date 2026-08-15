print("Welcome to the ITC245 FAQ Chatbot")
print("Type 'exit' to quit.\n")

while True:

    question = input("Ask a question: ").strip().lower()

    if question == "exit":
        print("Goodbye!")
        break

    elif "code" in question:
        print("Course Code: ITC245")

    elif "title" in question:
        print("Course Title: Artificial Intelligence Techniques")

    elif "lecturer" in question:
        print("Lecturer: Rishal Chand")

    elif "semester" in question:
        print("Semester: 2")

    elif "class time" in question or "time" in question:
        print("Class Time:")
        print("Lecture : 9:00 AM - 11:00 AM")
        print("Tutorial: 3:00 PM - 4:00 PM")
        print("Lab      : 11:00 AM - 1:00 PM")

    elif "course duration" in question or "duration" in question:
        print("Course Duration:")
        print("Lecture & Lab: 2 hours")
        print("Tutorial: 1 hour")

    elif "venue" in question or "classroom" in question or "room" in question:
        print("Venue:")
        print("Lecture : B105")
        print("Tutorial: B102")
        print("Lab      : C100")

    elif "assignment" in question:
        print("Assignments are available on Moodle.")

    elif "assessment" in question:
        print("The course has quizzes, labs, assignments and a final exam.")

    elif "lab" in question or "laboratory" in question:
        print("Labs help you practise programming.")

    elif "attendance" in question:
        print("Attendance is important for all classes.")

    elif "moodle" in question:
        print("Course materials are available on Moodle.")

    elif "software" in question:
        print("Required Software:")
        print("- Python")
        print("- Visual Studio Code")

    elif "submission" in question:
        print("Submit your work through Moodle.")

    elif "exam" in question or "final examination" in question:
        print("The final examination is held at the end of the semester.")

    elif "consultation" in question:
        print("Please contact your lecturer for student consultation.")

    elif "late" in question:
        print("Late submissions may receive penalties according to the course policy.")

    elif "ai" in question or "artificial intelligence" in question:
        print("Use Artificial Intelligence according to the course rules.")

    else:
        print("Sorry, I don't understand your question.")
        print("Please ask about:")
        print("- Course Code")
        print("- Course Title")
        print("- Semester")
        print("- Lecturer")
        print("- Class Time")
        print("- Course Duration")
        print("- Venue/Classroom")
        print("- Assessments")
        print("- Assignments")
        print("- Laboratory Activities")
        print("- Attendance")
        print("- Moodle")
        print("- Required Software")
        print("- Submission Process")
        print("- Final Examination")
        print("- Student Consultation")
        print("- Late Submission")
        print("- Artificial Intelligence")
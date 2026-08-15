print("=" * 50)
print("      ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'help' to see the list of questions.")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").lower().strip()

    if question == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    elif question == "help":
        print("""
Available questions:
- Course code
- Course title
- Semester
- Lecturer
- Class time
- Classroom
- Course duration
- Assessments
- Assignments
- Laboratory activities
- Attendance
- Moodle
- Required software
- Submission process
- Final examination
- Student consultation
- Late submission
- Use of Artificial Intelligence
""")

    elif "course code" in question:
        print("Chatbot: The course code is ITC245.")

    elif "course title" in question:
        print("Chatbot: The course title is Artificial Intelligence.")

    elif "semester" in question:
        print("Chatbot: This course is offered in Semester 2.")

    elif "lecturer" in question:
        print("Chatbot: The lecturer is Mr. Rajesh Singh.")

    elif "class time" in question:
        print("Chatbot: Monday, 10:00 AM to 12:00 PM.")

    elif "classroom" in question or "venue" in question:
        print("Chatbot: ICT Building, Lab 3.")

    elif "course duration" in question:
        print("Chatbot: The course lasts for 15 weeks.")

    elif "assessment" in question:
        print("Chatbot: The course has quizzes, labs,")
        print("assignments, and a final examination.")

    elif "assignment" in question:
        print("Chatbot: There are two assignments.")

    elif "laboratory" in question or "lab" in question:
        print("Chatbot: Laboratory sessions are held")
        print("every week.")

    elif "attendance" in question:
        print("Chatbot: Students should attend all")
        print("lectures and laboratory classes.")

    elif "moodle" in question:
        print("Chatbot: Moodle contains course notes,")
        print("announcements, and assignment details.")

    elif "software" in question:
        print("Chatbot: Install Python 3 and")
        print("Visual Studio Code.")

    elif "submission" in question:
        print("Chatbot: Submit assignments through")
        print("Moodle before the due date.")

    elif "final examination" in question or "exam" in question:
        print("Chatbot: The final examination is")
        print("held during the official exam period.")

    elif "consultation" in question:
        print("Chatbot: Consultation is on Wednesday")
        print("from 2:00 PM to 4:00 PM.")

    elif "late submission" in question:
        print("Chatbot: Late submissions may receive")
        print("a penalty unless approved.")

    elif "artificial intelligence" in question or "ai" in question:
        print("Chatbot: AI tools may be used only")
        print("according to the course AI policy.")

    else:
        print("Chatbot: Sorry, I don't understand.")
        print("Type 'help' to see available questions.")
print("<>" * 25)
print("      ITC245 COURSE FAQ CHATBOT")
print("<>" * 25)
print(" ")
print("Type 'exit' to close the chatbot.\n")
print("Type 'help' to view available questions.")

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
        print("CourseBot: Hello! Welcome to ITC245!.")

    elif "help" in question_lower:
        print("\nYou can ask questions about:")
        print("- Course code")
        print("- Course title")
        print("- Semester offered")
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

    elif "course code" in question_lower or "code" in question_lower:
        print("CourseBot: The course code is ITC245.")

    elif "coursebot" in question_lower or "bot" in question_lower:
        print("CourseBot: Yes? What can I help with?.")

    elif "your name" in question_lower or "name" in question_lower or "called" in question_lower or "call" in question_lower:
            print("CourseBot: My name is CourseBot! How can I help?.")    

    elif "course title" in question_lower or "title" in question_lower:
        print("CourseBot: The course title is Artificial Intelligence Techniques.")

    elif "semester offered" in question_lower or "semester" in question_lower:
        print("CourseBot: This course is offered in Semester 2.")

    elif "lecturer" in question_lower or "teacher" in question_lower:
        print("CourseBot: The lecturer for this course is Mr. Rishal Chand.")

    elif "class time" in question_lower or "time" in question_lower or "schedule" in question_lower:
        print("CourseBot:Your classes are at:\n The Lecture is on Tuesday, at 9:00 AM - 11:00 AM.\n The Tutorial is on Tuesday, at 3:00 PM - 4:00PM.\n The Lab is on Wednesday, at 11:00 AM - 1:00 PM")   

    elif "classroom" in question_lower or "venue" in question_lower or "room" in question_lower:
        print("CourseBot:Your classes are here:\n The Lecture is in B105.\n The Tutorial is in B102.\n The Lab is in C100")   

    elif "duration" in question_lower:
        print("CourseBot: This course is for 14 weeks.")

    elif "assessment" in question_lower or "assessments" in question_lower or "tests" in question_lower:
        print("CourseBot: Assessments include assignments, lab work, quizzes, and a final examination.")

    elif "assignment" in question_lower or "assignments" in question_lower or "projects" in question_lower:
        print("CourseBot: Assignment details will be available on Moodle/TopHat.")

    elif "lab" in question_lower or "laboratory" in question_lower:
        print("CourseBot: Laboratory sessions provide practical experience using AI tools and programming exercises.")

    elif "attendance" in question_lower:
        print("CourseBot: Students are expected to attend all lectures, tutorials and laboratory sessions.")

    elif "moodle" in question_lower or "course materials" in question_lower:
        print("CourseBot: Moodle is used for course materials, announcements, and assignment submissions.Just like TopHat.")

    elif "tophat" in question_lower or "TopHat" in question_lower or "course materials" in question_lower:
        print("CourseBot: TopHat is used for course materials, announcements, and assignment submissions. Just like Moodle.")

    elif "software" in question_lower or "required software" in question_lower:
        print("CourseBot: Required software includes Visual Studio Code, Python, and other software recommended by the lecturer.")

    elif "submission" in question_lower or "submit" in question_lower:
        print("CourseBot: Assignments should be submitted through Moodle/TopHat before the deadline.")

    elif "final exam" in question_lower or "exam" in question_lower or "finals" in question_lower:
        print("CourseBot: The final examination will be held during the official examination period in weeks 16 - 18.")

    elif "consultation" in question_lower or "consult" in question_lower:
        print("CourseBot: Students can meet the lecturer during consultation hours or by appointment.")

    elif "late submission" in question_lower or " Submit late" in question_lower:
        print("CourseBot: Late submissions may receive penalties unless an approved extension has been granted.")

    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("CourseBot: AI tools may only be used according to the course policy and lecturer's instructions.")

    elif "thank you" in question_lower or "thanks" in question_lower:
        print("CourseBot:You are very welcome :3")

    else:
        print("Assistant: Sorry, I do not know the answer. Please enter keywords.")

    print()
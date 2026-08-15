print("=" * 50)
print("ITC245 Course FAQ Chatbot")
print("Type 'exit' to end the chat.")
print("Type 'help' for assistance")
print("=" * 50)

while True:
    question = input("\nAsk a question: ").lower()

    if question == "exit":
        print("Chatbot: Thank you! Have a great day.")
        break

    elif "course code" in question or "code" in question:
        print("Chatbot: The course code is ITC245.")

    elif "course title" in question or "title" in question:
        print("Chatbot: The course title is Artificial Intelligence Techniques.")

    elif "semester" in question:
        print("Chatbot: This course is offered in Semester 2, 2026.")

    elif "lecturer" in question or "teacher" in question:
        print("Chatbot: The lecturer are Rishal Chand, Shamal Chand, Ashrita Kumar, Deepisha lata, Deepak Lal, Bimal Kumar, and Lubana Khan.")

    elif "class time" in question or "time" in question or "class" in question or "classroom" in question or "venue" in question or "room" in question:
        print("Chatbot: The classes are as followed...\nLecture classes: Tuesday \n  Time: 9am to 11am \n  Room: B105 \nTutorial classes: Tuesday \n  Time 3pm to 4pm \n  Room: B102 \nLab classes: Wednesday \n  Time: 11am to 1pm \n  Room: C100")

    elif "course duration" in question or "duration" in question:
        print("Chatbot: The course runs for 18 weeks.")

    elif "assessment" in question or "assessments" in question:
        print("Chatbot: Assessments include quizzes, assignments, lab exercises, and a final exam.")

    elif "assignment" in question or "assignments" in question:
        print("Chatbot: There are two major assignments during the semester.")

    elif "lab" in question or "laboratory" in question:
        print("Chatbot: Laboratory sessions involve practical Python programming and AI exercises.")

    elif "attendance" in question:
        print("Chatbot: Students are expected to attend all lectures and laboratory sessions.")

    elif "moodle" and "link" in question:
        print("Chatbot: The moodle and tophat links are:\nTophat : https://tophat.com/students/ \nMoodle link: https://elearning.unifiji.ac.fj/moodle/login/index.php.")

    elif "software" in question:
        print("Chatbot: Required software includes Python 3.x, VS Code or PyCharm, or use a website with python editor.")

    elif "submission" in question or "submit" in question:
        print("Chatbot: Assignments must be submitted through Moodle and Tophat before the deadline.")

    elif "final exam" in question or "exam" in question:
        print("Chatbot: The final examination will be held during the official examination period.")

    elif "consultation" in question or "office hour" in question:
        print("Chatbot: Student consultation hours are Wednesdays from 2:00 PM to 4:00 PM.")

    elif "late submission" in question or "late" in question:
        print("Chatbot: Late submissions may receive a penalty of 5% per day unless approved.")

    elif "artificial intelligence" in question or "ai" in question:
        print("Chatbot: AI tools may be used only according to the course policy. Always acknowledge any AI assistance and ensure your submitted work is your own.")

    elif "help" in question:
        print("\nYou can ask about:")
        print("- Course code")
        print("- Course title")
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

    else:
        print("Chatbot: Sorry, I don't understand that question. Type 'help' to see the available topics.")

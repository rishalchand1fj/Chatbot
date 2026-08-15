#Name: Sonia Lal
#ID: 20240056
#Course: ITC245
print("=" * 50)
print("ITC245 Course FAQ Chatbot")
print("Type 'exit' to end the chat.")
print("Type 'help' for assistance")
print("=" * 50)

while True:
    question = input("You: ").strip()
    question_lower = question.lower()
    

    if question_lower == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    elif "course code" in question_lower or "code" in question_lower:
        print("Assistant: Course code is ITC245.")
    elif "help" in question_lower:
        print("\nYou can ask about:")
        print("Course code")
        print("Course title")
        print("Semester")
        print("Lecturer")
        print("Class time")
        print("Classroom or venue")
        print("Course duration")
        print("Assessments")
        print("Assignments")
        print("Laboratory activities")
        print("Attendance")
        print("Moodle")
        print("Required software")
        print("Submission process")
        print("Final examination")
        print("Student consultation")
        print("Late submission")
        print("Use of Artificial Intelligence")
        
    elif "hi" in question_lower or "hello" in question_lower or "hey" in question_lower:
        print("Assistant: Hello! I am your assistant chatbot for ITC245.")
        print("How may I assist you?")

    elif "course title" in question_lower or "title" in question_lower or "course" in question_lower:
        print("Assistant: The course title is Artificial Intelligence Techniques.")

    elif "semester" in question_lower:
        print("Assistant: Course offered in Year 2 Semester 2")

    elif "lecturer" in question_lower or "teacher" in question_lower:
        print("Assistant: Lecturers are Rishal Chand, Shamal Chand, Ashrita Kumar, Deepisha lata, Deepak Lal, Bimal Kumar, and Lubana Khan.")
    
    elif "attendance" in question_lower:
        print("Assistant: Attendance for classes (Science/CS/IT) is compulsory. Students who fail to complete at least 80% of the practical requirements (including laboratory work) of a course shall be awarded a fail grade not with standing the fact that the student may have total marks for the continuous assessment and final examination which are equal to or greater than the pass mark (UniFiji 2026 Handbook & Calendar.")
        
    elif "class time" in question_lower or "time" in question_lower or "class" in question_lower or "classroom" in question_lower or "venue" in question_lower or "room" in question_lower:
        print("Assistant: Lecture \n-Room B105 \nTuesday 9am - 11am \nTutorial \n-Room B102 \nTuesday 3pm - 4pm \nLab \nRoom C100 \n-Wednesday 11am - 1pm")

    elif "course duration" in question_lower or "duration" in question_lower:
        print("Assistant: Duration of the course is for 18weeks.")

    elif "lab" in question_lower or "laboratory" in question_lower:
        print("Assistant: There will be a continuous two (2) hours lab per week for the course. The lab session will consist of practical demonstrations.")
        
    elif "assessment" in question_lower or "assessments" in question_lower:
        print("Assistant: Lab assessments will be conducted in the lab sessions. Students will be given small tasks that should be answered in two (2) hours or less as instructed by the lecturer. Marks will be given on the quality of work and accuracy of output.")

    elif "moodle" and "link" in question_lower:
        print("Assistant: Login to Tophat and Moodle using Student email. Here are the links:\nTophat : https://tophat.com/students/ \nMoodle link: https://elearning.unifiji.ac.fj/moodle/login/index.php.")

    elif "software" in question_lower or "app" in question_lower or "application" in question_lower:
        print("Assistant: Required software includes Python 3.x, VS Code or PyCharm, or use a website with python editor.")
 
    elif "late submission" in question_lower or "late" in question_lower:
        print("Assistant: Late submission of assignments will incur a penalty of 5 % of the marked assignment. No assignment will be accepted after the 7th day of the respective assessment due date.")
        
    elif "submission" in question_lower or "submit" in question_lower:
        print("Assistant: Submission dates will be provided as assignment are released.")

    elif "final exam" in question_lower or "exam" in question_lower:
        print("Assistant: Final exam will be held from week 16 to week 18 \n2 weeks of study time will be given.")

    elif "consultation" in question_lower or "office hour" in question_lower:
        print("Assistant: Consultation hours are from 11am - 1pm in Room B106")

    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("Assistant: Artificial intelligence (AI) is computer technology that mimics human thinking, learning, and problem-solving. People use AI to automate boring tasks, analyze big data, create content, and make fast choices in daily life and work.")

    else:
        print("Assistant: Sorry, I did not understand that. Can you try again...")

print("=" * 50)
print("      ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to close the chatbot. \n")
print("Type 'help' to view available questions.\n")

while True:
    question = input("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    if question == "":
        print("Assistant: Please enter a question. \n")
        continue

    if "hello" in question_lower or "hi" in question_lower:
        print("ITC245 Bot: Hello! Welcome to ITC245.")

    elif "help" in question_lower:
        print("\nYou can ask questions about:")
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
        print("- Withdrawal")
        print("- Use of Artificial Intelligence\n")

    elif "course code" in question_lower or "code" in question_lower:
        print("ITC245 Bot: The course code is ITC245.")

    elif "course title" in question_lower or "title" in question_lower or "course" in question_lower:
        print("ITC245 Bot: The course Title is Artificial Intelligence Techniques.")

    elif "semester" in question_lower or "which semester" in question_lower or "what semester" in question_lower:
        print("ITC245 Bot: The course is offered in Semester 2.")

    elif "lecturer" in question_lower or "teacher" in question_lower:
        print("ITC245 Bot: The lecturer is Mr. Rishal Chand.") 

    elif "class time" in question_lower or "time" in question_lower:
        print("ITC245 Bot: Classes are held on Tuesdays and Wednesdays, Tutorial is 1 hour on Tuesday(3-4pm in B102), Lecture is Two hours on Tuesday(9-11am in B105), And the lab is two hours on Wednesday(11-1pm in C100).")

    elif "classroom" in question_lower or "venue" in question_lower:
        print("ITC245 Bot: The venue of the Lecture is in B105, Tutorial is in B102 And the lab is in C100.") 

    elif "duration" in question_lower:
        print("ITC245 Bot: This course runs for 14 teaching weeks plus exams.")

    elif "assessments" in question_lower:
        print("ITC245 Bot: Assessments include Lab Assessment 1(5%) in Week 4, Lab Assessment 2(10%) in Week 11, MSE(20%) in Week 7, Tutorials & Participation (15%), and Final Exam (50%).")

    elif "assignments" in question_lower:
        print("ITC245 Bot: Assignments are lab activities submitted via Moodle or Tophat as part of continuous assessment.")

    elif "laboratory" in question_lower or "lab" in question_lower:
        print("ITC245 Bot: Laboratory activities involve practical AI exercises.")

    elif "attendance" in question_lower:
        print("ITC245 Bot: Attendance is compulsory where atleast Attendance of 80 percent in this course is required.")
 
    elif "moodle" in question_lower:
        print("ITC245 Bot: Course materials and submissions are managed via Moodle using your student ID and Password.")

    elif "software" in question_lower or "required software" in question_lower:
        print("ITC245 Bot: Required software includes Tophat and Moodle.")

    elif "submission" in question_lower:
        print("ITC245 Bot: Assignments must be submitted through Moodle or TopHat before the deadline.")

    elif "final exam" in question_lower or "examination" in question_lower:
        print("ITC245 Bot: The final examination is worth 50 percent of the total grade.")

    elif "consultation" in question_lower or "student consultation" in question_lower:
        print("ITC245 Bot: Consultation hours are TBA. You can contact Mr. Rishal Chand via mobile(6640600), email, or Viber groups. Room B110.")

    elif "late submission" in question_lower:
        print("ITC245 Bot: Late submissions incur a penalty of (5%) of the marked assignment. No assignment will be accepted after 7 days from the due date.")

    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("ITC245 Bot: The course covers classical AI concepts, search algorithms, probabilistic reasoning, and machine learning.")

    elif "withdraw" in question_lower or "drop" in question_lower or "unenroll" in question_lower:
        print("ITC245 Bot: Withdrawal requires informing the Registrar via prescribed form. Check Student Academic Services or the UniFiji Handbook for more details.")

    else:
        print("Assistant: Sorry, I do not know the answer. Type 'help' to see available questions.")

    print("-" * 50)

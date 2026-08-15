print("=" * 50)
print("            ITC245 FAQ CHATBOT")
print("=" * 50)
print("Welcome to the ITC245 Course Assistant")
print("Type 'help' to view available questions.")
print("Type 'exit' to close the chatbot.\n")

while True:
    question = input("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("ITC245 BOT: Goodbye! Have a nice day.")
        break

    if question_lower == "":
        print("ITC245 BOT: Please enter a question.\n")
        continue

    elif question_lower == "help":
        print("\nYou can ask about:")
        print("- Course code")
        print("- Course title")
        print("- Semester")
        print("- Lecturer")
        print("- Email")
        print("- Phone")
        print("- Consultation")
        print("- School")
        print("- Department")
        print("- Credit points")
        print("- Level")
        print("- Prerequisite")
        print("- Delivery mode")
        print("- Lecture hours")
        print("- Tutorial hours")
        print("- Lab practical")
        print("- Assessment")
        print("- Final exam")
        print("- Attendance")
        print("- Moodle")
        print("- Top Hat")
        print("- Top Hat join code")
        print("- Required software")
        print("- Submission")
        print("- Artificial Intelligence policy")
        print("- Classroom")
        print("- Course duration\n")

    elif "hello" in question_lower or "hi" in question_lower:
        print("ITC245 BOT: Hello! Welcome to the ITC245 FAQ Chatbot.")

    elif "course code" in question_lower:
        print("ITC245 BOT: The course code is ITC245.")

    elif "course title" in question_lower or "title" in question_lower:
        print("ITC245 BOT: The course title is Artificial Intelligence Techniques.")

    elif "semester" in question_lower:
        print("ITC245 BOT: This course is offered in Semester 2, 2026.")

    elif "lecturer" in question_lower or "coordinator" in question_lower or "teacher" in question_lower:
        print("ITC245 BOT: The Course Coordinator is Mr. Rishal Chand.")

    elif "email" in question_lower:
        print("ITC245 BOT: Email: rishalc@unifiji.ac.fj")

    elif "phone" in question_lower or "contact" in question_lower:
        print("ITC245 BOT: Phone: 6640600 Ext: 190")

    elif "consultation" in question_lower or "office" in question_lower:
        print("ITC245 BOT: Consultations are TBA. Contact Mr. Rishal Chand via email, mobile or Viber. Office: Room B110.")

    elif "school" in question_lower:
        print("ITC245 BOT: School of Science and Technology (SOST).")

    elif "department" in question_lower:
        print("ITC245 BOT: Department of Computer Science and Mathematics (CSM).")

    elif "credit" in question_lower:
        print("ITC245 BOT: The course is worth 15 Credit Points.")

    elif "level" in question_lower:
        print("ITC245 BOT: This is a Level 7 course.")

    elif "prerequisite" in question_lower or "requirement" in question_lower:
        print("ITC245 BOT: A pass in ITC106 is required before taking this course.")

    elif "delivery" in question_lower or "mode" in question_lower:
        print("ITC245 BOT: Delivery Mode: Face-to-Face.")

    elif "lecture" in question_lower:
        print("ITC245 BOT: Lectures are 2 hours per week.")

    elif "tutorial" in question_lower:
        print("ITC245 BOT: Tutorials are 1 hour per week.")

    elif "lab" in question_lower or "practical" in question_lower:
        print("ITC245 BOT: Lab Practical sessions are 2 hours per week.")

    elif "assessment" in question_lower:
        print("ITC245 BOT: Continuous Assessment = 50%, Final Examination = 50%.")

    elif "assignment" in question_lower:
        print("ITC245 BOT: Assignment details will be provided by the lecturer during the semester.")

    elif "attendance" in question_lower:
        print("ITC245 BOT: Students are expected to attend all lectures, tutorials and laboratory sessions.")

    elif "moodle" in question_lower:
        print("ITC245 BOT: Course materials and announcements will be available on Moodle.")

    elif "software" in question_lower:
        print("ITC245 BOT: You will need Python and Visual Studio Code for laboratory activities.")

    elif "submission" in question_lower:
        print("ITC245 BOT: Assignment submission instructions will be provided by the lecturer.")

    elif "late" in question_lower:
        print("ITC245 BOT: Please consult the course coordinator regarding the late submission policy.")

    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("ITC245 BOT: Artificial Intelligence tools should only be used according to the lecturer's instructions and University policies.")

    elif "final" in question_lower or "exam" in question_lower:
        print("ITC245 BOT: The Final Examination is worth 50% of the course grade.")

    elif "top hat" in question_lower and "code" in question_lower:
        print("ITC245 BOT: The Top Hat Join Code is 668825.")

    elif "top hat" in question_lower:
        print("ITC245 BOT: ITC245 uses Top Hat for class participation. Join Code: 668825.")

    elif "classroom" in question_lower or "venue" in question_lower or "room" in question_lower:
        print("ITC245 BOT: Your lecturer will inform you of the classroom or venue.")

    elif "duration" in question_lower:
        print("ITC245 BOT: The course runs during Semester 2, 2026.")

    else:
        print("ITC245 BOT: Sorry, I don't understand that question. Type 'help' to see available questions.")



    


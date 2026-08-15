print("=" * 50)
print("             ITC245 COURSE FAQ CHATBOT")
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
        print("ITC245 Bot: Hello! Welcome to ITC245.")

  
    elif "help" in question_lower:
        print("\nYou can ask questions about:")
        print("- Course code / title")
        print("- Semester / Course duration")
        print("- Lecturer / Student consultation")
        print("- Class time / Classroom (venue)")
        print("- Assessments / Assignments / Laboratory activities / Final exam")
        print("- Attendance / Moodle / Required software")
        print("- Submission process / Late submission")
        print("- Use of AI\n")

    
    elif "course code" in question_lower or "code" in question_lower:
        print("ITC245 Bot: The course code is ITC245.")
    elif "title" in question_lower or "name of course" in question_lower:
        print("ITC245 Bot: The course title is Artificial Intelligence Techniques .")

   
    elif "semester" in question_lower:
        print("ITC245 Bot: This course is offered in Semester 2.")
    elif "duration" in question_lower:
        print("ITC245 Bot: The course duration is 14 weeks.")

    
    elif "lecturer" in question_lower or "teacher" in question_lower or "professor" in question_lower:
        print("ITC245 Bot: The course lecturer is Mr Rishal.")
    elif "consultation" in question_lower:
        print("ITC245 Bot: Student consultation hours are Tuesdays and Thursdays from 2:00 PM - 4:00 PM.")

    
    elif "time" in question_lower or "schedule" in question_lower:
        print("ITC245 Bot: Class takes place on Mondays and Wednesdays from 10:00 AM to 12:00 PM.")
    elif "venue" in question_lower or "classroom" in question_lower or "room" in question_lower or "location" in question_lower:
        print("ITC245 Bot: The classroom venue is Lab 3, ICT Building.")

    
    elif "assessment" in question_lower or "grading" in question_lower:
        print("ITC245 Bot: Coursework counts for 50% and the Final Exam counts for 50%.")
    elif "assignment" in question_lower:
        print("ITC245 Bot: There are 2 major assignments throughout the semester.")
    elif "lab" in question_lower or "laboratory" in question_lower:
        print("ITC245 Bot: Weekly lab activities are held in Lab 3 and submitted via Moodle.")
    elif "exam" in question_lower or "final" in question_lower:
        print("ITC245 Bot: The final exam is a 3-hour written and practical examination at the end of the semester.")

    
    elif "attendance" in question_lower:
        print("ITC245 Bot: Minimum required attendance is 80% for both lectures and labs.")
    elif "moodle" in question_lower:
        print("ITC245 Bot: You can access all lecture slides, labs, and announcements on the ITC245 Moodle page.")
    elif "software" in question_lower:
        print("ITC245 Bot: Required software includes Python 3.x and Visual Studio Code.")
    elif "late" in question_lower:
        print("ITC245 Bot: Late submissions incur a 10% penalty per day unless an extension is granted.")
    elif "submission" in question_lower or "submit" in question_lower:
        print("ITC245 Bot: All submissions must be uploaded directly to Moodle before the deadline.")

    
    elif "ai" in question_lower or "artificial intelligence" in question_lower:
        print("ITC245 Bot: AI tools may be used for learning and assistance, but all submitted code must be your own work.")

    
    else:
        print("Assistant: Sorry, I do not know the answer.")

    print()
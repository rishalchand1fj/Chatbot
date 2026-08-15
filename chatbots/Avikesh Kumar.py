# Welcome to JDoodle!
#
# You can execute code here in 110+ languages. Right now you’re in the Python3 IDE.
#
#  1. Click the orange Execute button ️▶ to execute the sample code below and see how it works.
#  2. Want help writing or debugging code? Type a query into JDroid on the right hand side ---------------->
#
# Want to change languages? Try the search bar up the top.
print("=" * 50)
print("           ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'help' to view available questions.")
print("Type 'exit' to close the chatbot.\n")

while True:
    question = input("You: ").strip()
    question_lower = question.lower()

  
    if question_lower == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break


    if question == "":
        print("Assistant: Please enter a question.\n")
        continue

    if question_lower in ["hi", "hello", "hey"]:
        print("Assistant: Hello! Welcome to the ITC245 Course FAQ Chatbot.")

  
    elif "help" in question_lower:
        print("\nYou can ask questions about:")
        print("- Course code")
        print("- Course title")
        print("- Semester")
        print("- Lecturer")
        print("- Class time")
        print("- Lab Class time")
        print("- Tutorial Class time")
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
        print("- Use of Artificial Intelligence")

  
    elif "course code" in question_lower or "code" in question_lower:
        print("Assistant: The course code is ITC245.")

    elif "course title" in question_lower or "title" in question_lower:
        print("Assistant: The course title is Artificial Intelligence Techniques.")

    elif "semester" in question_lower:
        print("Assistant: This course is offered in Semester 2, 2026.")

    elif "lecturer" in question_lower or "teacher" in question_lower or "who teaches" in question_lower:
        print("Assistant: The lecturer is Rishal Chand.")

  
    elif "lab class time" in question_lower or "lab time" in question_lower:
        print("Assistant: Lab classes are held every Wednesday from 11:00 AM to 1:00 PM.")

    elif "tutorial class time" in question_lower or "tutorial time" in question_lower:
        print("Assistant: Tutorial classes are held every Tuesday from 03:00 PM to 04:00 PM.")

    elif "class time" in question_lower or "lecture time" in question_lower:
        print("Assistant: Lectures are held every Tuesday from 9:00 AM to 11:00 AM.")


    elif "classroom" in question_lower or "venue" in question_lower or "room" in question_lower:
        print("Assistant: Classes are conducted in Room B105.")

  
    elif "duration" in question_lower:
        print("Assistant: The course runs for 15 weeks.")


    elif "assessment" in question_lower or "assessments" in question_lower:
        print("Assistant: Assessments include assignments, lab work, and a final examination.")


    elif "assignment" in question_lower or "assignments" in question_lower:
        print("Assistant: There are two Lab Assessments and one Mid-Semester Exam (MSE).")

  
    elif "lab" in question_lower or "laboratory" in question_lower:
        print("Assistant: Weekly laboratory sessions provide practical programming exercises.")

  
    elif "attendance" in question_lower:
        print("Assistant: Students are expected to attend all lectures, labs, and tutorials.")

 
    elif "moodle" in question_lower:
        print("Assistant: Course submissions and announcements are available on Moodle.")


    elif "software" in question_lower:
        print("Assistant: You should install Python 3 and Visual Studio Code.")


    elif "submission" in question_lower or "submit" in question_lower:
        print("Assistant: Assignments must be submitted through Moodle before the deadline.")

    elif "exam" in question_lower or "final examination" in question_lower:
        print("Assistant: The final examination will be held during the official examination period.")


    elif "consultation" in question_lower or "office hour" in question_lower:
        print("Assistant: Student consultation is available every Wednesday from 2:00 PM to 4:00 PM.")

    elif "late" in question_lower:
        print("Assistant: Late submissions may receive penalties unless an approved extension has been granted.")


    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("Assistant: AI tools may only be used according to the course guidelines and academic integrity policy.")

   
    else:
        print("Assistant: Sorry, I couldn't find an answer to that. Type 'help' to see the available questions.")

    print()   

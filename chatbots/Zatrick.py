print ("-"*50)
print ("     CHAT WITH ITC245 COURSE FAQ CHATBOT")
print ("-"*50)
print ("Type 'exit' to close the chatbot.")
print ("Type 'help' to view available questions.\n")

while True:
    question = input ("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print ("ITC245 BOT: Goodbye! Have a nice day. :)\n")
        break

    if question == "":
        print("ITC245 BOT: Please Enter Something! :)")
        continue

    if "hellow" in question_lower or "hi" in question_lower:
        print ("ITC245 BOT: Hellow! Welcome to the ITC245 Course Unit. How may I help you today! ;)")

    elif "help" in question_lower:
        print("\nYou can ask ITC245 BOT questions about: ")
        print("- Course Code")
        print("- Course title")
        print("- Semester")
        print("- Lecturer")
        print("- Class time")
        print("- Venue or Classroom")
        print("- Course duration")
        print("- Assessments")
        print("- Assignments")
        print("- Laboratory activities")
        print("- Attendance")
        print("- Moodle")
        print("- Required software")
        print("- Submission process")
        print("- Final examination")
        print("- Student consulation")
        print("- Late submission")
        print("- Use of Artificial Intelligence")
        


    elif "course code" in question_lower or "code" in question_lower:
        print ("ITC245 BOT: The Course Code is ITC245.")

    elif "course title" in question_lower or "title" in question_lower:
        print("ITC245 BOT: The Course title is Artificial Intelligence Techniques - S2/2026.")

    elif "Semester" in question_lower or "semester" in question_lower:
        print("ITC245 BOT: The course can be available in semester 2 2026. ")
    
    elif "Lecturer" in question_lower or "lecturer" in question_lower:
        print("ITC245 BOT: The Lecturer is Mr.Rishal Chand.")
    
    elif "Class Time" in question_lower or "time" in question_lower:
        print("ITC245 BOT: Tuesday 9-11am is the lecture class for this course. It is mandatory for all students taking this course to attend since it is only for this day.")

    elif "classroom" in question_lower or "venue" in question_lower:
        print("ITC245 BOT: Classes are held in room B105.")
    
    elif "Course duration" in question_lower or "duration" in question_lower:
        print("ITC245 BOT: The course duration is the whole of this semester.")
    
    elif "Assessments" in question_lower or "assessments" in question_lower:
        print("ITC245 BOT: There are 2 assessments throughout the course duration.")

    elif "Assignments" in question_lower or "assignments" in question_lower:
        print("ITC245 BOT: There is 1 assignment throughout this course duration")

    elif "Laboratory activities" in question_lower or "lab" in question_lower:
        print("ITC245 BOT: Laboratory activities are done each week throughout the whole semester both practical and theory.")

    elif "Attendance" in question_lower or "attendance" in question_lower:
        print("ITC245 BOT: Attendance is taken online via a code during, before or after each lesson whether tutorial, lab or lecture.")

    elif "Moodle" in question_lower or "moodle" in question_lower:
        print("ITC245 BOT: Course materials are provided and submissions.")

    elif "Required Software" in question_lower or "software" in question_lower:
        print("ITC245 BOT: The softwares include vscode and visual studio 2022.")

    elif "Submission process" in question_lower or "submission" in question_lower:
        print("ITC245 BOT: Work submissions can be done in TopHat or Moodle.")

    elif "Final examination" in question_lower or "exam" in question_lower:
        print("ITC245 BOT: There is a MST on week 7 of this course semester and a final examination at the end of the course semester.")

    elif "Student consultation" in question_lower or "consultation" in question_lower:
        print("ITC245 BOT: Students can have consulations any time throughout the week.")

    elif "Late submissions" in question_lower or "Late" in question_lower:
        print("ITC245 BOT: Students will be penalized with late submissions.")

    elif "Use of Artificial Intelligence" in question_lower or "ai" in question_lower:
        print("ITC245 BOT: It depends entirely on the specifications of the task or activity that is introduced within the course.")
        

    else:
        print("ITC245 BOT: Sorry! I do not know the answer. Try asking something else. :)")

    print()


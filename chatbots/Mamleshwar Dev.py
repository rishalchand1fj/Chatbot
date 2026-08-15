print(" Welcome to the ITC245 FAQ Chatbot ")
print(" Type 'exit' to quit.")

while True:
    question = input("\nAsk a question: ").strip().lower()

    if question == "exit":
        print("Goodbye! Have a great day.")
        break

    elif "course code" in question or "code" in question:
        print("Course Code: ITC245")

    elif "course title" in question or "title" in question:
        print("Course Title:Artificial Intelligence Techniques ")

    elif "semester" in question:
        print("Semester: 2")

    elif "lecturer" in question:
        print("Lecturer: RISHAL CHAND")

    elif "class" in question or "time" in question:
        print("Class Time: LECTURE 9-11 ")
        print("Class Time: TUTORIAL 3-4 ")
        print("Class Time: LAB 11-1 ")


    elif "room" in question or "classroom" in question:
         print("Class Time: LECTURE B105 ")
         print("Class Time: TUTORIAL B102 ")
         print("Class Time: LAB C100 ")

    elif "assessment" in question:
        print("Assessments: week 4 ")
        print("Assessments: week 11 ")

    elif "attendance" in question:
        print("Attendance is expected for all lectures and labs.")

    elif "moodle" in question:
        print("Course materials are available on Moodle.")

    elif "software" in question:
        print("Required Software: Python 3 and Visual Studio Code.")

    elif "submit" in question or "submission" in question:
        print("Submit assignments through Moodle before the deadline.")

    elif "exam" in question or "final" in question:
        print("Final examination details will be announced by the lecturer.")

    elif "consultation" in question:
        print("Consult the lecturer during consultation hours.")

    elif "late" in question:
        print("Late submissions may receive penalties according to the course policy.")

    elif "artificial intelligence" in question or "ai" in question:
        print("Use of AI must follow the course guidelines provided by the lecturer.")

    else:
        print("Sorry, I don't understand that question. Please ask about the ITC245 course.")
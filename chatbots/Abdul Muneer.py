print("*"* 50)
print("Hello, I'm your ITC 245 chatbot! How can I assist you today?")
print("*"* 50)

while True:
    question = input("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break

    if question_lower =="":
        print("Chatbot: Please enter a question or type 'exit' to quit.")
        continue

    elif "hello" in question_lower or "hi" in question_lower:
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in question_lower:
        print("Chatbot: I'm just a program, How can I assist you?")

    elif "what is your name" in question_lower:
        print("Chatbot: I'm your ITC 245 chatbot!")

    elif "course code" in question_lower or "code" in question_lower:
        print("Chatbot: The course code is ITC245.")

    elif "course title" in question_lower or "title" in question_lower or "name" in question_lower or "course" in question_lower:
        print("Chatbot: The course title is Artificial Intelligence Techniques.")

    elif "semester" in question_lower:
        print("Chatbot: This course is offered in Semester 2, 2026.")
    elif "lecturer" in question_lower or "instructor" in question_lower or "teacher" in question_lower:
        print("Chatbot: Your course coordinator is Mr. Rishal Chand.")

    elif "class time" in question_lower or "time" in question_lower or "schedule" in question_lower:
        print("Chatbot: Lectures are on Tuesday from 9:00 AM to 11:00 AM. Labs are on Tuesday from 11:00 AM to 1:00 PM. Tutorials are on Thursday from 3:00 PM to 4:00 PM.")

    elif "venue" in question_lower or "classroom" in question_lower or "room" in question_lower:
        print("Chatbot: Lectures are in B105, Labs are in C100, and Tutorials are in B104.")

    elif "duration" in question_lower:
        print("Chatbot: The course has 2 hours of lectures, 1 hour of tutorial, and 2 hours of lab practical each week.")

    elif "assessment" in question_lower:
        print("Chatbot: The course consists of 50% continuous assessment and 50% final examination.")

    elif "assignment" in question_lower:
        print("Chatbot: Assessment details are available on Moodle and will be explained by the lecturer.")

    elif "lab" in question_lower or "laboratory" in question_lower:
        print("Chatbot: Lab practicals are held every Tuesday from 11:00 AM to 1:00 PM in C100.")

    elif "attendance" in question_lower:
        print("Chatbot: Attendance is compulsory. You must complete at least 80% of the practical requirements.")

    elif "moodle" in question_lower:
        print("Chatbot: Moodle is used for course materials and Turnitin submissions.")

    elif "software" in question_lower:
        print("Chatbot: The required software will be installed during the first laboratory session.")

    elif "submit" in question_lower or "submission" in question_lower:
        print("Chatbot: All assessments must be submitted through Turnitin on Moodle.")

    elif "final exam" in question_lower or "exam" in question_lower:
        print("Chatbot: The final examination is worth 50%. The timetable will be announced by the university.")

    elif "consultation" in question_lower or "consult" in question_lower:
        print("Chatbot: Consultation is available by contacting Mr. Rishal Chand via email, mobile, or the Viber group.")

    elif "late" in question_lower:
        print("Chatbot: Late submissions receive a 5% penalty per assignment and are not accepted after seven days.")

    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("Chatbot: AI tools may be used responsibly according to your lecturer's instructions and university academic integrity policies.")

    else:
        print("Chatbot: I'm sorry, I don't have an answer for that. Please ask another question or type 'exit' to quit.")
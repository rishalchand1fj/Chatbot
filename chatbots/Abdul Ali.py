print("*" * 50)
print("Welcome to the ITC245 Chatbot!")

def get_response(user_input):
    text = user_input.lower()

    # Course information
    if "course code" in text or "code" in text and "itc245" in text:
        return "Chatbot: The course code is ITC245."
    if "course title" in text or "title" in text:
        return "Chatbot: The course title is Artificial Intelligence and Techniques."
    if "semester" in text:
        return "Chatbot: The course is offered in the current semester as listed in the timetable and course outline."
    if "lecturer" in text or "teacher" in text:
        return "Chatbot: The lecturer is the instructor assigned to ITC245 for this semester."
    if "class time" in text or "time" in text and "class" in text:
        return "Chatbot: Please check your timetable or Moodle for the exact class time."
    if "venue" in text or "classroom" in text or "room" in text:
        return "Chatbot: Your classroom or venue is listed in your timetable or on Moodle."
    if "duration" in text or "length" in text:
        return "Chatbot: The course runs for the full semester."
    
    # Assessments and learning activities
    if "assessment" in text or "assessments" in text:
        return "Chatbot: Assessments may include tests, quizzes, assignments, practical work, and other tasks listed in the course outline."
    if "assignment" in text or "assignments" in text:
        return "Chatbot: Assignments are usually submitted through Moodle unless your lecturer gives other instructions."
    if "laboratory" in text or "lab" in text:
        return "Chatbot: Laboratory activities are part of the course and may be assessed."
    if "attendance" in text:
        return "Chatbot: Attendance is expected. Please attend all scheduled classes and laboratory sessions."
    
    # Online learning and tools
    if "moodle" in text:
        return "Chatbot: Moodle is used for announcements, lecture materials, assignments, and submission links."
    if "software" in text or "required software" in text:
        return "Chatbot: The required software will be listed in the course outline or announced on Moodle."
    
    # Submission and exams
    if "submission" in text or "submit" in text:
        return "Chatbot: Submit your work through Moodle before the deadline and follow the instructions for each task."
    if "final exam" in text or "examination" in text or "exam" in text:
        return "Chatbot: The final examination is scheduled by the university timetable. Check Moodle and the official exam timetable."
    if "consultation" in text or "office hours" in text:
        return "Chatbot: Consultation hours are usually posted on Moodle or can be arranged with the lecturer."
    if "late submission" in text or "late" in text and "submission" in text:
        return "Chatbot: Late submissions may be penalized according to the course policy, so please check the course outline."
    
    # AI policy
    if "artificial intelligence" in text or "ai" in text or "chatgpt" in text:
        return "Chatbot: Use of AI must follow the lecturer’s guidance and the university’s academic integrity policy."

    # Greetings and help
    if "hello" in text:
        return "Chatbot: Hello! How can I assist you today?"
    if "help" in text:
        return "Chatbot: Sure! I can help with ITC245 course code, assessments, Moodle, submission, exams, and more."
    
    return "Chatbot: I’m not sure how to answer that. Please ask about the course code, title, timetable, assessments, Moodle, exams, or submission."

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    print(get_response(user_input))
print("*50")
print("welcome to ITC245 Chatbot")

while True:
    question=input("You:").strip()
    question_lower=question.lower()

    if question_lower=="exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    elif question_lower == "hello":
        print("Assistant: Hello! How can I assist you today?")

    elif "course code" in question_lower or "code" in question_lower:
        print("Assistant: The course code for ITC245 is ITC245.")

    elif "course name" in question_lower or "name" in question_lower:
        print("Assistant: The course name for ITC245 is \"Artificial Intelligence Fundamentals\".")

    elif "instructor" in question_lower or "lecturer" in question_lower:
        print("Assistant: The instructor for ITC245 is Mr. Rishal.")

    elif "class schedule" in question_lower or "schedule" in question_lower:
        print("Assistant: The class schedule for ITC245 is Monday and Wednesday from 10:00 AM to 11:30 AM.")

    elif "semester" in question_lower and "duration" in question_lower and "offered" in question_lower:
        print("Assistant: The ITC245 course is offered in semester 2 and its duration is 16 weeks.")

    elif "moodle link" in question_lower or ("link" in question_lower and "moodle" in question_lower):
        print("Assistant: The Moodle link for ITC245 is https://moodle.example.com/itc245.")

    elif "assignment" in question_lower and "submission" in question_lower and "link" in question_lower:
        print("Assistant: The assignment submission link for ITC245 is https://moodle.example.com/itc245/assignments.")

    elif "exam" in question_lower and "schedule" in question_lower and "link" in question_lower:
        print("Assistant: The exam schedule link for ITC245 is https://moodle.example.com/itc245/exams.")

    elif "ai use" in question_lower and "in" in question_lower and "ai detection"in question_lower:
        print("Assistant: AI can be used in various ways, including natural language processing, computer vision, and predictive analytics. AI detection refers to the process of identifying and analyzing AI-generated content or behaviors.")
    else:
        print("Assistant: I'm sorry, I don't have information on that. Please type 'exit' to end the conversation or ask another question.")
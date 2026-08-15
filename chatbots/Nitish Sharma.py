print("========================================")
print("       ITC245 FAQ CHATBOT")
print("========================================")
print("Hello! I can answer questions about ITC245.")
print("Type 'exit' to close the chatbot.\n")

while True:
    question = input("Student: ").strip().lower()

    if question == "exit":
        print("Chatbot: Thank you for using the ITC245 FAQ Chatbot. Goodbye!")
        break

    elif "course code" in question or "code" in question:
        print("Chatbot: The course code is ITC245.")

    elif "course title" in question or "title" in question:
        print("Chatbot: The course title is Artificial Intelligence Techniques.")

    elif "semester" in question:
        print("Chatbot: ITC245 is offered in Semester 2, 2026.")

    elif "lecturer" in question or "teacher" in question:
        print("Chatbot: The Course Coordinator is Mr. Rishal Chand, Assistant Lecturer in Computer Science.")

    elif "class time" in question:
        print("Chatbot: Lecture: Tuesday 9am - 11pm, Lab: Wednesday 11am - 1pm, Tutorial: Tuesday 3pm - 4pm")
    elif "classroom" in question or "venue" in question or "room" in question:
        print("Chatbot: Lecture - B105, Lab - C100, Tutorial - B102")
    elif "course duration" in question:
        print("Chatbot: 13 Weeks")
    elif "assessment" in question or "assessments" in question:
        print("Chatbot: Assessment consists of Lab Assessments (15%), MSE (20%), Tutorial and Participation (15%), and Final Examination (50%).")
    elif "assignment" in question or "assignments" in question:
        print("Chatbot: Assessment details are provided on Moodle. Lab Task 1 covers Weeks 1-4 and Lab Task 2 covers Weeks 5-11.")
    elif "laboratory activities" in question or "lab" in question:
        print("Chatbot: There is a continuous 2-hour lab each week. Lab sessions consist of practical demonstrations.")
    elif "attendance" in question:
        print("Chatbot: Attendance is compulsory. Students must complete at least 80% of practical requirements, including laboratory work.")
    elif "moodle" in question:
        print("Chatbot: Moodle is used for the course. All assessments are submitted through Turnitin, which is available through Moodle.")
    elif "required software" in question:
        print("Chatbot: The required software are Visual Studio Code, Python, Moodle and Top Hat")
    elif "submission process" in question or "submit" in question:
        print("Chatbot: All assessments are submitted through Turnitin via Moodle or Top Hat.")
    elif "final examination" in question or "final exam" in question or "exam" in question:
        print("Chatbot: The final examination is worth 50% and is scheduled for Weeks 17-18. The exact date and time will be advised later.")
    elif "student consultation" in question or "consult" in question:
        print("Chatbot: Consultation is TBA. Students can contact Mr. Rishal Chand via mobile, email, and Viber groups. His consultation room is B110.")
    elif "late submission" in question or "late" in question:
        print("Chatbot: Late assignments receive a 5% penalty of the marked assignment. No assignment will be accepted after the 7th day after its due date.")
    elif "artificial intelligence" in question or "ai" in question:
        print("Chatbot: AI Ethics and Responsible Use is covered in Week 13. Students should follow the course and University policies regarding responsible AI use.")
    elif "top hat" in question:
        print("Chatbot: Top Hat is used for class participation and in-class questions. The ITC245 Top Hat join code is 668825.")
    elif "course coordinator" in question:
        print("Chatbot: The Course Coordinator is Mr. Rishal Chand, MINFITC, PGDITC, BIT, UniFiji.")
    elif "credit" in question or "credit point" in question:
        print("Chatbot: ITC245 is worth 15 credit points.")
    elif "prerequisite" in question:
        print("Chatbot: The prerequisite for ITC245 is a pass in ITC106.")
    elif "delivery" in question:
        print("Chatbot: The delivery mode is Face to Face.")
    elif "topics" in question or "course content" in question:
        print("Chatbot: Topics include Artificial Intelligence, Generative AI Tools, Large Language Models, Prompt Engineering, Machine Learning, Supervised and Unsupervised Learning, Computer Vision, Image Classification and Processing, NLP, and AI Ethics.")
    elif "pass" in question or "passing" in question:
        print("Chatbot: Students must achieve at least 40% in coursework and 40% in the final examination, and a total of 50% to pass the course.")
    else:
        print("Chatbot: Sorry, I do not understand that question.")
        print("Chatbot: Please ask a question related to ITC245.")
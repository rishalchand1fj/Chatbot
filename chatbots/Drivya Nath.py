print("=" * 50)
print("Welcome to ITC245 ChatBot")

while True:
    question = input("You: ").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print("Bot: Goodbye!")
        break
    elif question == "":
        print("Bot: enter something")
    elif "hi" in question_lower or "hello" in question_lower:
        print("BOT: welcome to ITC245, how can i help you?")
    elif "course code" in question_lower or "code" in question_lower:
        print("Bot: the course code is ITC245")
    elif "course title" in question_lower or "title" in question_lower:
        print("Bot: the course title is Artificial Intelligence Techniques")
    elif "semester" in question_lower:
        print("Bot: this course is offered in Semester 2, 2026")
    elif "lecturer" in question_lower:
        print("Bot: the lecturer for this course is Mr.Rishal Chand")
    elif "class time" in question_lower or "time" in question_lower:
        print("Bot: classes are held on Tuesday - lecture at 9-11am, Tuesday-Tutorial at 3.4pm and wednesday lab at 11-1")
    elif "classroom" in question_lower or "venue" in question_lower:
        print("Bot: classes are held in lecture - B105, Tutorial- B102, Lab-C100")
    elif "duration" in question_lower:
        print("Bot: this course runs for 18 weeks including exams")
    elif "assessment" in question_lower:
        print("Bot: assessments include mid semester exams, 2 lab assessments, and a final exam")
    elif "assignment" in question_lower:
        print("Bot: there are several assignments during the semester")
    elif "lab" in question_lower:
        print("Bot: laboratory activities are held weekly and are compulsory")
    elif "attendance" in question_lower:
        print("Bot: attendance is compulsory, at least 80% required")
    elif "moodle" in question_lower:
        print("Bot: course materials and submissions are all on Moodle")
    elif "software" in question_lower:
        print("Bot: you will need Python and Visual Studio Code")
    elif "late" in question_lower:
        print("Bot: late submissions have a penalty of 5% unless an extension is approved and no assignment would be accepted after the 7th day of its due date")
    elif "submission" in question_lower:
        print("Bot: assignments must be submitted through Moodle or tophat before the deadline")
    elif "exam" in question_lower:
        print("Bot: the final examination covers all topics")
    elif "consultation" in question_lower:
        print("Bot: student consultation can be done through email, face to face, contact via mobile, viber groups")
    elif "ai" in question_lower or "artificial intelligence" in question_lower:
        print("Bot: use of AI must be disclosed and follow academic integrity policy")
    else:
        print("BOT: sorry i dont have the answer, type HELP")
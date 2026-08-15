print("=== ITC245 FAQ CHATBOT ===\n")
print("Type 'exit' to quit\n")
print("Type 'hi' to greet the bot\n")
print("Type 'help' to view available questions\n")

while True:
    q = input("You: ").lower()

    if q == "exit":
        print("Bot: Goodbye!")
        break
    elif q == "help":
        print("\nAvailable questions:")
        print("- What is the course code?")
        print("- What is the course title?")
        print("- When is the course offered?")
        print("- Who is the lecturer?")
        print("- What are the class times and venues?")
        print("- What is the course duration?")
        print("- What assessments are there?")
        print("- Are there any assignments?")
        print("- What about lab sessions?")
        print("- Is attendance required?")
        print("- Where can I find course materials?")
        print("- What software do I need?")
        print("- How do I submit assignments?")
        print("- What is the exam structure?")
        print("- Can I get consultation with the lecturer?")
        print("- What are the consequences of submitting late?")
        print("- How should I use AI in my work?")

    elif "course code" in q:
        print("Bot: The course code is ITC245.")

    elif "hi" in q:
        print("Bot: Hi there! How can I help you with today?")

    elif "course title" in q:
        print("Bot: The course title is Artificial Intelligence Techniques.")

    elif "semester" in q:
        print("Bot: This is Semester 1, 2026")

    elif "lecturer" in q:
        print("Bot: Your lecturer is Mr. Rishal Chand.")

    elif "time" in q:
        print("Bot: Lecture is on Tuesday from 9.00 AM to 11.00 AM in B105\nTutorial is on Monday from 3.00 PM to 4.00 PM in B104\nLab is on Wednesday from 11.00 AM to 1.00 PM in C100")

    elif "classroom" in q or "venue" in q:
        print("Bot: Lecture is in B105\nTutorial is in B104\nLab is in C100")

    elif "duration" in q:
        print("Bot: This course is provided in Semester 2, 2026")

    elif "assessment" in q:
        print("Bot: Includes assignments, labs, and exam")

    elif "assignment" in q:
        print("Bot: There are no assignments for this course")

    elif "lab" in q:
        print("Bot: There is a weekly lab sessions once a week for 2 hours. Lab sessions are held on Wednesday from 11.00 AM to 1.00 PM in C100")

    elif "attendance" in q:
        print("Bot: Attendance is required")

    elif "moodle" in q:
        print("Bot: Use Moodle and Tophatfor materials and submissions")

    elif "software" in q:
        print("Bot: Use VS Code with Python extensions")

    elif "submission" in q:
        print("Bot: Submit via Moodle and Tophat")

    elif "exam" in q:
        print("Bot: Final exam at end of semester\nShort test in week 7")

    elif "consultation" in q:
        print("Bot: Contact lecturer during office hours")

    elif "late" in q:
        print("Bot: Late submissions may get penalties and points deducted")

    elif "ai" in q:
        print("Bot: AI use must follow university rules")

    else:
        print("Bot: Sorry, I don't understand, please try again.")
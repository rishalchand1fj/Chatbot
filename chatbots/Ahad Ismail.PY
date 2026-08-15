print("=" * 50)
print("            ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to close the chatbot.\n")
print("Type 'help' to view available questions.")

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
        print("- Course code")
        print("- Course title")
        print("- Lecturer name")
        print("- Lecturer email / contact")
        print("- Lab schedule")
        print("- Lecture schedule")
        print("- Tutorial schedule")
        print("- Prerequisite")
        print("- Credit points")
        print("- Assessment breakdown")
        print("- MSE (mid-semester exam)")
        print("- Final exam")
        print("- Late submission penalty")
        print("- Referencing style")
        print("- Top Hat join code")
        print("- Textbook")

    elif "course code" in question_lower or ("code" in question_lower and "top hat" not in question_lower):
        print("ITC245 Bot: The course code is ITC245.")

    elif "course title" in question_lower or "title" in question_lower:
        print("ITC245 Bot: The course title is Artificial Intelligence Techniques - S2/2026.")

    elif "email" in question_lower or "contact" in question_lower:
        print("ITC245 Bot: Email rishalc@unifiji.ac.fj, Phone 6640600 Ext 190, Room B110.")

    elif "lecturer" in question_lower:
        print("ITC245 Bot: The lecturer is Mr. Rishal Chand.")

    elif "lab" in question_lower:
        print("ITC245 Bot: Lab is in room C100, Wednesday 11am to 1pm.")

    elif "lecture" in question_lower:
        print("ITC245 Bot: Lecture is in room B105, Tuesday 9am to 11am.")

    elif "tutorial" in question_lower:
        print("ITC245 Bot: Tutorial is in room B104, Tuesday 3pm to 4pm.")

    elif "prerequisite" in question_lower:
        print("ITC245 Bot: Prerequisite is a Pass in ITC106.")

    elif "credit" in question_lower:
        print("ITC245 Bot: Credit Points (CP) = 15.")

    elif "assessment" in question_lower or "breakdown" in question_lower:
        print("ITC245 Bot: Lab Assessment 15%, MSE 20%, Tutorial/Participation 15%, Final Exam 50%.")

    elif "mse" in question_lower or "mid" in question_lower:
        print("ITC245 Bot: MSE is in Week 7, worth 20%.")

    elif "final exam" in question_lower or "exam" in question_lower:
        print("ITC245 Bot: Final Exam is in Week 17-18, worth 50%.")

    elif "late" in question_lower or "penalty" in question_lower:
        print("ITC245 Bot: Late submissions incur 5% penalty per day, not accepted after 7 days.")

    elif "reference" in question_lower or "referencing" in question_lower:
        print("ITC245 Bot: This course uses Harvard referencing style.")

    elif "top hat" in question_lower or "tophat" in question_lower:
        print("ITC245 Bot: Top Hat join code for ITC245 is 668825.")

    elif "textbook" in question_lower or "book" in question_lower:
        print("ITC245 Bot: Textbook - Russell & Norvig, Artificial Intelligence: A Modern Approach, 4th edition, Pearson.")

    else:
        print("Assistant: Sorry, I do not know the answer.")

    print()
print("=" * 50)
print ("ITC245 COURSE FAQ CHATBOT")
print ("=" * 50)
print ("Type 'exit' to close chatbot.\n")
print ("Type 'help' to view available question.")

while True:
    question =input("You:").strip()
    question_lower = question.lower()

    if question_lower == "exit":
        print ("Bot: Goodbye! Have a nice day.") 
        break
    if question == "":
        print("Bot: Please enter a question.\n")
        continue
    if "hello" in question_lower or "hi" in question_lower:
        print ("ITC245 Bot: Hello! Welcome to ITC245.")
    elif "help" in question_lower:
        print("\nYou can ask question about:")
        print("-course code")
        print("-course Title")
    elif "code" in question_lower or "code course" in question_lower:
        print("ITC245 Bot: the course code is ITC245")  
    elif "Course title" in question_lower or "title" in question_lower:
        print("Bot: Artifical Intelligence Techniques")
    elif "semester" in question_lower :
        print ("Bot: Semester 2")
    elif "lecturer" in question_lower:
        print("Bot: Rishal Chand") 
    elif "class time" in question_lower or "venue" in question_lower:
        print ("Bot: Lecture on Tuesday 9am - 11am Room:B105") 
        print ("Bot: Tutorial on Tuesday 3pm - 4pm Room:B102") 
        print ("Bot: Lab on Wednesday 11am - 1pm Room:C100")
    elif "assessment" in question_lower or "assignment" in question_lower or "lab activity" in question_lower:
        print("Bot: Please login into your tophat and moddle for more information")
    elif "course duration " in question_lower or " duration" in question_lower:
        print("Bot: 3 Years of Course")
    elif "attendance" in question_lower:
        print ("Bot: Login to your tophat\n enter your course code\n add the course \n find the classroom (where the lecture presenting the slide) \n you can mark your self present")
    elif "moddle" in question_lower or "required software" in question_lower or "software" in question_lower:
        print("Bot: look for an IT staff their will help")
    elif "sumbmission process" in question_lower or "submission" in question_lower or "ai" in question_lower or "artifical intelligence" in question_lower or "late submission" in question_lower :
        print("Bot: Please login into your tophat and moddle for more information" )
    elif "final examination" in question_lower or "student consultation" in question_lower:
         print("Bot: look for course outline give by the lecturer Or look for the lecturer to ask for consultation" )
    else:
        print( "Bot: Sorry, I do not know the answer.")    
    print()
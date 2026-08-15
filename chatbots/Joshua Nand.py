print("=" * 50)
print("         ITC245 COURSE FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to close the chatbot.\n")
print("Type 'help' to view available questions.")

while True:
    question = input("You: ").strip()
    question_lower = question.lower()
    
    if question_lower == "exit":
        print("Assistant: Ab Toh Hoye Ge")
        break
    
    if question == "":
        print("Assistant: Please enter a question.\n")
        continue
    
    if "hello" in question_lower or "hi" in question_lower:
        print("ITC245 Bot: Hello! Welcome to ITC245.")
        
    elif "help" in question_lower:
        print("\nYou can ask questions about:")
        print("- Course code")
        print("-Course title ")
        print("- Semester")
        print("- Lecturer")
        print("- Class Time")
        print("- Classroom/Venue")
        print("- Course duration")
        print("- Assesments")
        print("- Assignments")
        print("- Labrotary Activities")
        print("- Attendance")
        print("- Moodle")
        print("- Required software")
        print("- Submission process")
        print("- Final examination")
        print("- Student consultation")
        print("- Late submission")
        print("- Use of AI")
        
        
    elif "course code" in question_lower or "code" in question_lower:
        print("ITC245 Bot: The course code is ITC245.")
        
    elif "course titile" in question_lower or "title" in question_lower:
        print("ITC245 Bot: ARTIFICIAL INTELLEGENCE")
        
    elif "semester" in question_lower:
        print("2")
        
    elif "lecturer" in question_lower:
        print("Rishal Chand")
        
    elif "class time" in question_lower:
        print("starts at 9am to 4pm")
        
    elif "classroom" in question_lower or "class" in question_lower:
        print("Lecture-B105")
        print("Lab- C100")
        print("Tutorial- B102")
        
    elif "duration" in question_lower:
        print("Lecture and Labs- 2 Hours")
        print("Tutorials- 1 hour")
        
    elif "assesment" in question_lower:
        print("Mid semester and finalz")
        
    elif "assingments" in question_lower:
        print("given during labs")
        
    elif "laboratory activities" in question_lower:
        print("depends on the lecture based questions")
        
    elif "attendance" in question_lower:
        print("given to students who attend")
        
    elif "moodle" in question_lower:
        print("accessed by registered students")
        
    elif "required software" in question_lower:
        print("VS Code")
        
    elif "submission process" in question_lower:
        print("Through Moodle")
        
    elif "final examination" in question_lower:
        print("week 16 of semester 2")
        
    elif "student consultation" in question_lower:
        print("registers office near boys washroom")
        
    elif "late submission" in question_lower or "late" in question_lower:
        print("marks deducted")
        
    elif "use of ai" in question_lower:
        print("should be below 20%")
        
    
    
        
    
    
    else:
        print("Assistant: Sorry, I didnt get you.")
        
    print()
    
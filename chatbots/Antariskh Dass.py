print("="* 50)
print("        ITC245 COURSE FAQ CHATBOT")
print("="* 50)
print("type 'exit' to close the chatbot.\n")
print("type 'help' to view available questions.")

while True:
    question= input("you: ").strip()
    question_lower= question.lower()
    
    if question_lower == "exit":
        print("assistent: please enter a question")
        continue
    elif "hello" in question_lower or "hi" in question_lower:
        print("ITC245 BOT: Hello! welcome to ITC245.")
        
    elif "help" in question_lower:
        print("you can ask question about:")
        print("- course code")
        print("- course title")
    
    elif "course code" in question_lower or "code" in question_lower:
        print("ITC245 Bot: the course code is ITC245.")
    
    elif "semester" in question_lower:
        print("ITC245 Bot:semester 2.")
    
    elif "lecturer" in question_lower:
        print("ITC245 Bot:The lecturer for ITC245 is Rishal.")
        
    elif "classroom" in question_lower or "class time" in question_lower or "venue" in question_lower:
        print("ITC245 Bot:The class time for ITC245 is from 9 to 11am in the classroom B104")
    
    elif "course duration" in question_lower:
        print("ITC245 Bot:the course duration for ITC245 is for 6 months.")
    
    elif "assessment" in question_lower or "assignments" in question_lower:
        print("ITC245 Bot:the assessment for ITC245 will take place in week 7 and the assignments will be done in week 4.")
    
    elif "laboratory" in question_lower or "lab" in question_lower:
        print("ITC245 Bot: the laboratory activities will take place every Wednesday.")
    
    elif "attendance" in question_lower:
        print("ITC245 Bot:Attendance will be taken every class and is important for the coursework")
    
    elif "moodle" in question_lower:
        print("ITC245 Bot:Assignments will be uploaded on moodle where AI detection will be checked")
    
    elif "required software" in question_lower or "software used" in queestion_lower:
        print("ITC245 Bot: The software to be used in ITC245 is python.")
    
    elif "submission process" in question_lower or "submission" in question_lower:
        print("ITC245 Bot:Submissions are to be uploaded to moodle or tophat.")
    
    elif "final examination" in question_lower:
        print("ITC245 Bot:The final examination dates are not yet confrimed.")
    
    elif "student consultation" in question_lower:
        print("A student consultation for ITC245 is where students can meet their lecturer Mr.Rishal to ask questions.")
    
    elif "late submissions" in question_lower: 
        print("ITC245 Bot:For ITC245, Late submissions follow the unit policy, please seek help from lecturer")
    
    elif "use of artificial intelligence" in question_lower or "AI" in question_lower:
        print("ITC245 Bot: Artificial intelligence is a tool that can help you learn or solve problems, but use it carefully. In ITC245, use AI to support your work, not to replace it.")
    
    else: 
        print("Assistant: sorry, I do not know the answer.")
    
    print()    
    
        
    
        
    

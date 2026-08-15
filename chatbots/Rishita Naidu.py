while True:
    question = input("you: "). strip()
    question_lower = question.lower()
    
    if question_lower == "exit":
        print("Assistant: Goodbye! have a nice day.")
        break
    
    if question == "":
        print("Assistant: please enter a question.\n")
        continue
    
    if "code" in question_lower or "course" in question_lower:
        print("course code  : ITC245.")
        
    elif "semester" in question_lower:
        print("ITC245  : semester2.") 
        
    elif " course title" in question_lower:
        print("title   : ARTIFICIAL INTELLIGENCE.")
        
    elif "lecturer" in question_lower:
        print(" lecturer is  :  MR RISHAL.")
        
    elif "class time" in question_lower:
        print("class time : LEC- FROM 9-11 ON TUESDAYS,TUT- FROM 3-4 ON TUESDAYS AND LABS ON WEDNESDAY- FROM 11-1.")
        
    elif " clssroom venue" in question_lower:
        print("venue for classes are:   LEC- B105, TUT- B102, LABS- C100.")
        
    elif "course duration" in question_lower:
        print(" course duration will be: from wk 1-16. wk 1-7 NORMAL LECTURES, WK 8 MSB, WK 9-14 NORMAL CLASSES, WK 15 MSB, AND WK 16-18 EXAMINATION.")
        
    elif "Assessment" in question_lower:
        print(" assessment will be in:  wk 4 Lab Assessment 1 5%, wk 7 MSE 20%, wk 11 Lab Assessment 2 10%")
        
    elif "assignments" in question_lower:
        print("will be compiled using: HARVARD REFRENCING")
        
    elif "lab activities" in question_lower:
        print("lab activities: will be done during the lab classes and submitted either on moodle or tophat")
        
    elif "Attendance" in question_lower:
        print("attendace will be considered as: Attendance for classes (Science/CS/IT) is compulsory. ")

    elif "Moodle" in question_lower:
        print("moodle is a platform where: Assignments will be submitted through Moodle (Turnitin). where the rate should be below 20% ")
        
    elif "Required software" in question_lower:
        print(" required software are: Turnitin, tophat and Microsoft Word (.doc or .docx).")
        
    elif "submission process" in question_lower:
        print("All submissions will be done through:  Uploaded in Turnitin on Moodle in Word format.") 
        
    elif "Final EXAMINATION" in question_lower:
        print("all final examinations will be conducted in:   week 16 to week 18")
        
    elif "student consultation" in question_lower:
        print("student consultation:   not yet mentioned")
        
    elif "late submission"in question_lower:
        print("All late submission:  A penalty of 5% will be deducted ")
        
    elif "AI usage" in question_lower:
        print("AI usage:    basically this course is based on AI usage, how to use it effectively")
        
        
        
        
        
        
              
        
    
    
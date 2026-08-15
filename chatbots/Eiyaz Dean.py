print("=" * 50)
print("welcome to ITC 245 Course FAQ Chatbot")

while True: 
    question = input("You: ").strip()
    question_lower = question.lower()

    if "hello" in question_lower or "bula" in question_lower or "hi" in question_lower or "hey" in question_lower:
        print("Aj Yaad kiya Tum neh.")
    elif "course code" in question_lower or "code" in question_lower:
        print("ITC245  : The Course Code is ITC245 ")
    elif "title" in question_lower or "long Form" in question_lower:
        print("Bot : The Title is Artifical Intelligence ")
    elif "lecturer" in question_lower or "professor" in question_lower or "teacher" in question_lower:
        print("The Course Coordinator for this Course is Mr Rishal Chand")
    elif "ok" in question_lower or "oh" in question_lower:
        print("Is there anything else you would like to ask")
    elif "yes" in question_lower or "think" in question_lower or "may" in question_lower or "yes please" in question_lower:
        print("Alright please state your question and i'll Happliy assist you")
    elif " class" in question_lower or "time" in question_lower:
        print("""The classes are as follows: 
              
        "Tuesday Lecturer from 9Am - 11Am in Room B105"
        "Wednesday Tutorial from 12pm-1pm in Room B102" 
        "Thursday Lab from 1pm-3pm in LAb C100
        """)
    elif "venue" in question_lower or "room" in question_lower or "location" in question_lower:
        print("The classes are held in the following venues: \n"
              "Lecturer: Room B105 \n"
              "Tutorial: Room B102 \n"
              "Lab: Lab C100")
    elif "course duration" in question_lower or "duration" in question_lower or "length" in question_lower:
        print("The course duration is 12 weeks")    
    elif "assessment" in question_lower or "assessments" in question_lower or "grading" in question_lower:
        print("The assessments for this course are as follows: \n"
              "1. Assignment 1: 20% \n"
              "2. Assignment 2: 20% \n"                                         
                "3. Final Exam: 60% \n")    
    elif "lab" in question_lower or "labs" in question_lower:
        print("The labs for this course are held on Thursdays from 1pm-3pm in Lab C100")    
    elif "tutorial" in question_lower or "tutorials" in question_lower:
        print("The tutorials for this course are held on Wednesdays from 12pm-1pm in Room B102")    
    elif "attendance" in question_lower or "participation" in question_lower:
        print("Attendance is mandatory for all classes, and participation is encouraged.")
    elif "moodle" in question_lower or "online" in question_lower or "platform" in question_lower:
        print("The course materials and resources are available on the Moodle platform.")   
    elif "requirements" in question_lower or "prerequisites" in question_lower:
        print("The prerequisites for this course are: \n"
              "1. Basic programming knowledge \n"
              "2. Understanding of algorithms and data structures \n")
    elif "submission" in question_lower or "submit" in question_lower or "deadline" in question_lower:
        print("The submission deadlines for assignments will be announced in class and on Moodle.")
    elif 'final exam' in question_lower or 'exam' in question_lower or 'final' in question_lower:
        print("The final exam will be held during the exam period at the end of the semester.") 
    elif "office hours" in question_lower or "consultation" in question_lower:
        print("The lecturer's office hours are on Tuesdays from 11am-12pm and Thursdays from 3pm-4pm.") 
    elif "contact" in question_lower or "email" in question_lower or "phone" in question_lower:
        print("You can contact the course coordinator via email at coordinator@university.edu or by phone at (123) 456-7890.")  
    elif "late submission" in question_lower or "late" in question_lower:
        print("Late submissions will incur a penalty as per the course policy. Please refer to the syllabus for details.")  
    elif "artificial intelligence" in question_lower or "ai" in question_lower:
        print("Artificial Intelligence (AI) is a branch of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence, such as visual perception, speech recognition, decision-making, and language translation.") 
    elif "thank you" in question_lower or "thanks" in question_lower:
        print("You're welcome! If you have any more questions, feel free to ask.")  
    else:
        print("I'm sorry, I don't have information on that topic. Please ask another question or refer to the course syllabus for more details.")   

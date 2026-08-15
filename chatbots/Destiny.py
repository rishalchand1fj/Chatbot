print("=" * 50)
print("=======                                   =======")
print("=======    ITC245 COURSE FAQ CHATBOT      =======")
print("="*50)
print("Hello,Bula,halo!")
print("\n type'exit' to close the chatbot.")
print ("Type 'help' to view available questions.")

while True:
    question = input("\n You: ").strip()
    question_lower = question.lower()
    
    if question_lower=="exit":
        print("assistant:goodbye! Have a blessed day")
        break
    
    if question=="":
        print("assistant:please feel free to enter a question a question you want to proceed with. .")
        continue
    
    if "hello" in question_lower or "hi" in question_lower or "bula"in question_lower:
          print("ITC245 Bot: Hello,Bula,Halo! Welcome to ITC245. ")
          
    elif "help" in question_lower:
        print("\nYou can ask questions about :")
        print("- Course code")
        print("- course title or what is the course title")
        print("- semester")
        print("-  lecturer")
        print("- class time, classroom")
        print("- course duration")
        print("- assessment")
        print("- asignment")
        print("- laboratory activities")
        print("- attendance")
        print("- about moodle")
        print("- required software or what software is required for submission")
        print("- Submission process")
        print("- final  examination")
        print("- student consultation")
        print("-late submission or consequence of late submission")
        print("- use of artificial intelligence/what is the use of artificial intelligence")
    
    
    
    elif "course code" in question_lower or "code" in question_lower :
          print("ITC245 Bot: The course code is ITC245.\n ")
          
    elif "course title" in question_lower or"what is the course title" in question_lower:
          print("course title is Artificial Intelligence techniques.\n")
    
    elif "semester"in question_lower or  "in what semester" in question_lower:
          print(" semester: two(2)")
    
    elif "who is the lecturer for that course" in question_lower or "lecturer" in question_lower:
          print("Lecturer for ITC245 is= Mr. Rishal chand")

    elif "class time for the course and classroom" in question_lower or "course time, classroom" in question_lower:
           print("\ntuesday:9-11am_ROOM B105")
           print("wednesday:11am -1pm_ROOM B105\n")

    elif "what is the course duration" in question_lower or "course duration" in question_lower:
           print("\n The course Duration ")
           print("\n LECTURE(lecture will takes 14weeks of that semester & 2hrs per week= 28hrs total in whole semester)")
           print(" Tutorial/Discussion Forums (will take 13weeks of that semester & 1hr per week=13hrs total in whole semester)")
           print("\n LAB (will take 13weeks & 2hrs per week= 26hrs total in whole semester) ") 
           print("\n TOTAL=67hrs to takes in ITC245 course in 1 whole semester + extra given for study(158)=__225hrs in total____  ")

    elif"course assessment" in question_lower or "assessment" in question_lower:         
          print("The ITC245  Assessment breakdown are as follow.\n")
          print("ASSESSMENT______________________DUE DATE________________WEIGHT(%)")
          print("LAB ASSESS                      WK4, WK11                   15%")
          print("MSE                             WK7                         20%")
          print("Tutorial participation          WK1-15                      15%")
          print("Final exam                      WK17 & 18                   20%\n")

    elif "how many assignment are there ont that course" in question_lower or "assignment" in question_lower:
          print("There is no assignment for this course ONLY Assessment\n")

    elif "laboratory activities" in question_lower:
          print(" There are 11 lab activities with 2 major lab assessment")

    elif "how many attendance are all together for this course" in question_lower or "Total attendance" in question_lower:
          print("Individual attendance to Lectures, Tutorials, and Labs is recorded every week ")
          print("for 14 weeks=42 attendence(include lecture/tutorial/lab)")

    elif "moodle" in question_lower or "about moodle" in question_lower: 
          print("Moodle (an online course management system) can be accessed from the following link: https://elearning.unifiji.ac.fj/moodle")
          print("Or by clicking on the “Moodle” link on the University’s website.")
          print("you can access using you Your IDusername")
          print("for your Password for first yr you will be required to change your password after your initial login. Your new password must be at least 8 characters long including letters and numbers.")

    elif"how to use moodle for sumbmission" in question_lower:
          print("Click on the assignment dropbox: This will open a new page")
          print("Add Submission: Click on 'Add Submission'")
          print("Upload your file: You can either click on 'Add a file' or drag and drop your file into the box")
          print("After uploading your file, click on save and upload to submit")
          print("Turnitin: Your assignment will go through Turnitin, which may take approximately 60sec/1 or 2 minutes. Once submitted, no further changes are")

    elif "required software" in question_lower:
          print("tophat & moodle ")

    elif"submission process" in question_lower:
          print("\n Submission process")
          print("submit answers to in-class questions using  smartphones,tablets and other devices, through tophat((https://success.tophat.com/s/article/Student-Getting-Startedwith-Top-Hat))")
          print("AND using moodle for checking turnitin(http://elearning.unifiji.ac.fj/moodle/)")

    elif"when is the final examination" in question_lower or "final examination" in question_lower:
          print("will be either in week 17 or 18")
          print("final examination=50%")
          print("best to achieve minimum of 40% in coursework and 40% in examination in order to pass the course ")

    elif"student consultation" in question_lower:
          print("Consultations: TBA [Contact via mobile, email, and Viber groups], Room: B110")

    elif"consequence of late submission" in question_lower or "late submission" in  question_lower:
          print("the consequence of late submission will result with 5% penalty of the mark assignment. But if after 7th days then no more assignment will be accepted.")
          print("NOTE: if you caught serious illness in any submission or schedule of an assessment or assignment then YOUR NEED to PROVIDE a proper MEDICAL CERTIFICATES ")

    elif"what is the use of artificial intelligence" in question_lower or "use of artificial intelligence" in question_lower:
         print("Artificial Intelligence (AI) is used to help computers perform tasks that normally require human intelligence, making work faster, easier, and more accurate.")
         print("accurate in a way of:")
         print("Answer questions")
         print("Recognize speech and images (voice assistants, face recognition)")
         print("Recommend products or videos (YouTube, Netflix, online shopping)")
         print("Translate languages")
         print("Automate repetitive work in businesses and factories")
         print("help doctors in diagonose the disease in a patient \n")
         print("with this course it help the student to understand the use of AI")
         print("")
       
else: 
      print("Assistant: Sorry, I do not know the answer.")

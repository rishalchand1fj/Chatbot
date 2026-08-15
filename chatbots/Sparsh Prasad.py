print ("*" *50)
print ("   ITC 245 CHAT BOX   ")
print ("*" *50)
print (" type 'EXIT' to close the chatbox.")
print (" type 'HELP' to view available  questions in the chatbox")

while True:
    question = input(" ").strip()
    question_lower = question.lower()

    if question_lower == "EXIT":
        print (" bot: i hope i was able to help you out with what you were looking for.\n goodbye! have a great day.")
        break

    if question == "help":
        print("bot: how can i help you today?\nyou can ask about the following:\nCourse code\nCourse title\nsemester\nLecturer\nClass time\nClassroom or venue\nCourse duration\nAssessments\nAssignments\nLaboratory activities\nAttendance\nMoodle\nRequired software\nSubmission process\nFinal examination\nStudent consultation")
        continue

    if "hi" in question_lower or "hello" in question_lower:
        print (" chat bot avaiable for your assistance.\n how can i help you? ")

    elif "course code" in question_lower:
         print (" chat bot: the course code is ITC 245")

    elif "title" in question_lower or " course title" in question_lower:
             print (" chat bot: the course title is  Artificial Interlligence Techniques")

    elif "semester" in question_lower:
             print ("chat bot:  this is semester 2 for the year 2026")

    elif "lecturer" in question_lower or "coordinator" in question_lower or "teacher" in question_lower:
             print ("chat bot: the lecturer for this course is Mr Rishal ")

    elif "time table" in question_lower or "class time" in question_lower:
             print ("chat bot: \ntuesday 9am to 11am lecture\ntuesday 3pm to 4pm tutorial\nwednesday 11am to 1pm lab")

    elif "room" in question_lower or "venue" in question_lower:
                 print ("chat bot: \ntuesday 9am to 11am lecture is in room B105\ntuesday 3pm to 4pm tutorial is in room B102\nwednesday 11am to 1pm lab is in room C100")
    
    elif "unit duration" in question_lower or "how long is course" in question_lower:
                 print ("chat bot: 3 yrs")

    elif "assessment" in question_lower or "assignment" in question_lower or "laboratory" in question_lower or "lab" in question_lower:
                 print ("chat bot: please login into tophat and moodle for more information")

    elif "attendance" in question_lower:
                 print ("chat bot: \nlogin to your tophat\n enter your course\n look for grade book ( usually at the top right conner)\n you may find attendance there.")

    elif "moodle" in question_lower or "required sofware" in question_lower:
                 print ("chat bot: please look for an IT STAFF  to help you out")
    
    elif "exam" in question_lower or " exam time table" in question_lower:
                     print ("chat bot: please login into unifiji website or\n login to your email for all information")

    
    elif "late submission" in question_lower or "submission" in question_lower or"ai" in question_lower or " Artificial interigence" in question_lower:
                         print ("chat bot: please ask your lecturer regrading AI and late submission as different lecturers have differnt options.")  


    else :
            print ( "chat box: sorry, i do not understand you.")
    print()
print("=" * 50)
print("=                                                =")
print("=   ITC245 Artificial Intelligence Techniques    =")
print("=                                                =")
print("="* 50)
print("type 'exit' to close the chatbot. \n")
print("Type 'help' to view available questions.")

while True :
    question = input ("You: ").strip ()
    question_lower = question.lower()
    
    if question_lower == "exit":
        print ("Assistant: Goodbye! Have a nice day.")
        break
    
    if question == "":
        print("Please enter a question.\n")
        continue
    
    if "hello" in question_lower or "hi"in question_lower: 
        print("ITC245 Bot: Hello! Welcome to ITC245.")
        
    elif "help" in question_lower :
        print("\nYou can ask questions about:")
        print("- Course code")
        print("- Course title")
        print("- Semester")
        print("- Lecturer")
        print("- class time")
        print("- Classroom ")
        print("- Course duration")
        print("- Assesment")
        print("- Assignments")
        print("- Laboratory activities")
        print("- Attendance")
        print("- Moodle")
        print("- Required software")
        print("- Submission process")
        print("- Final examination")
        print("- Student consultation")
        print("- Late submission")
        print("- Use of Artificial Intelligence")
        
    elif "course code" in question or "code" in question_lower:
        print("ITC245 Bot: The course code is ITC245.")
        
    elif "course title" in question or "title" in question_lower:
         print("ITC245 Bot: The course title is 'Artificial Intelligence Techniques' .")
            
    elif "semester" in question or "sem" in question_lower:
        print("ITC245 Bot: The course is offered in semester 2.")   
            
    elif "lecturer" in question or "lec" in question_lower:
        print("ITC245 Bot: The lecturer of this coure is MR.Rishal Chand .") 
                       
    elif "class time" in question or "time"in question_lower:
        print("ITC245 Bot: Their are 3 three classes you need to attend:\n -Lecture in room B105 at Tuesday from 9am - 11am\n -Tutorial in room B102 at Tuesdsay from 3pm - 4pm\n -Lab in room C100 at Wednesday from 11am - 1pm")
    
    elif "classroom" in question or "venue"in question_lower:
         print("ITC245 Bot: Their are 3 three classes you need to attend:\n -Lecture in room B105 at Tuesday from 9am - 11am\n -Tutorial in room B102 at Tuesdsay from 3pm - 4pm\n -Lab in room C100 at Wednesday from 11am - 1pm")
            
    elif "class duration" in question or "duration"in question_lower:
        print("ITC245 Bot: The course is for the whole of the semester ")
    
    elif "assessments" in question or "assess"in question_lower:
        print("ITC245 Bot: Student performance is assessed entirely by continuous internal assessment throughout the course.\nStudents will be assessed as follows:\nAssessment Item                    Due Date          Weight (%)\nLab Assessment                     Week4 & week 11    15%\nMSE                                Week7              20%\nTutortial & Participation          Week 1 -15         15%\nFinal Exam                         Week 17 & 18       50%\n               TOTAL                                  100%")
                
    elif "Use of artificial intelligence" in question or "ai" in question_lower:
        print("ITC245 Bot: \na) When a marker finds a student of plagiarism or collusion, the piece of academic work MUST be brought to the attention of the course coordinator concerned.\nb) The course coordinator will endeavour to locate the sources from which this student has plagiarized. If satisfied that the student has plagiarized, the course coordinator\n   will collate the evidence of the breach for record purposes and submit the evidence at the earliest opportunity to the respective Deans. It will include a copy of the academic work\n   and a list of sources, page numbers, and/or copies of the plagiarized sources.\nc) The student will be notified by the Head of School and issued with an official letter stating the allegations and giving him/her the opportunity to present his/her case.\nd) If the Dean is satisfied that the student has engaged unknowingly in such behaviours, he/she may implement a penalty according to the provisions of 3.0 below.")
        
    elif "late submission" in question or "late" in question_lower:
         print("ITC245 Bot: Late submission of assignments will incur a penalty of 5% of the marked assignment. No assignment will be accepted after the 7th day of the respective assessment due date.")
         
    elif "student consultation" in question or "consultation" in question_lower:
        print("ITC245 Bot: There are two main types of support: Academic Advising/Enrolment Counselling and Personal Welfare Support (Mental Health Counselling).") 
        
    elif "final examination" in question or "examination" in question_lower:
        print("ITC245 Bot: Final Examination - Exam Date/ Time (Examination Timetable will be advised later). A student need to have  ")
        
    elif "submission process" in question or "submission" in question_lower:
        print("ITC245 Bot: All assessments for the course will be submitted through Turnitin which shall be available on Moodle and on Tophat.")
        
    elif "required software" in question or "software" in question_lower:
        print("ITC245 Bot: Students are required to install viber as a mean for communication.\nTophat for viewing and submiting answers of the course")
        
    elif "moodle" in question or "moodel" in question_lower:
        print("ITC245 Bot: Moodle will be made available through the Moodle website (http://elearning.unifiji.ac.fj/moodle/). All assessments for the course will be submitted through Turnitin which shall be available on Moodle")
        
    elif "attendance" in question or "attend" in question_lower:
        print("ITC245 Bot: Individual attendance to Lectures, Tutorials, and Labs is recorded every week")
        
    elif "laboratory activities" in question or "lab activities" in question_lower:
        print("ITC245 Bot: Students are given tasks to test their knowledge of what they have covered in weeks 1-11")
        
    elif "assignments" in question or "assign" in question_lower:
        print("ITC245 Bot: Their are 2 assignments you need to attend before the Mid-Semester Break and 1 assignments after the break.\n-Lab Assessment 1 (5%)\n-MSE (20%)\n-Lab Assessment 2 (10%)")
                        
    

print()
        
           

# ==========================================
# ITC245 Course FAQ Chatbot
# Week 3 Lab
# ==========================================

print("=" * 55)
print("      Welcome to the ITC245 FAQ Chatbot")
print("=" * 55)

while True:

    print("\nPlease choose an option:")
    print("1. Course Code")
    print("2. Course Title")
    print("3. Semester")
    print("4. Lecturer")
    print("5. Class Time")
    print("6. Classroom/Venue")
    print("7. Course Duration")
    print("8. Assessments")
    print("9. Assignments")
    print("10. Laboratory Activities")
    print("11. Attendance")
    print("12. Moodle")
    print("13. Required Software")
    print("14. Submission Process")
    print("15. Final Examination")
    print("16. Student Consultation")
    print("17. Late Submission")
    print("18. Use of Artificial Intelligence")
    print("19. Exit")

    choice = input("\nEnter your choice (1-19): ").strip()

    if choice == "1":
        print("\nChatbot: The course code is ITC245.")

    elif choice == "2":
        print("\nChatbot: The course title is Artificial Intelligence Techniques.")

    elif choice == "3":
        print("\nChatbot: This course is offered in Semester 2.")

    elif choice == "4":
        print("\nChatbot: The lecturer is Rishal Chand.")

    elif choice == "5":
        print("\nChatbot: Classes are held on Wednesday from 9:00 AM to 11:00 AM.")

    elif choice == "6":
        print("\nChatbot: Classes are held in Room B105.")

    elif choice == "7":
        print("\nChatbot: The course runs for one semester.")

    elif choice == "8":
        print("\nChatbot: Assessments include assignments, labs, quizzes, and the final examination.")

    elif choice == "9":
        print("\nChatbot: Assignment details are available on Moodle.")

    elif choice == "10":
        print("\nChatbot: Laboratory sessions provide practical programming experience.")

    elif choice == "11":
        print("\nChatbot: Students are expected to attend all lectures and labs.")

    elif choice == "12":
        print("\nChatbot: Course materials, announcements, and submissions are available on Moodle.")

    elif choice == "13":
        print("\nChatbot: You will need Visual Studio Code and Python installed.")

    elif choice == "14":
        print("\nChatbot: Submit your work through Moodle or TopHat before the deadline.")

    elif choice == "15":
        print("\nChatbot: The final examination will be scheduled by the university.")

    elif choice == "16":
        print("\nChatbot: Please contact the lecturer to arrange a consultation.")

    elif choice == "17":
        print("\nChatbot: Late submissions may receive penalties according to the course policy.")

    elif choice == "18":
        print("\nChatbot: AI tools may only be used according to the course guidelines.")

    elif choice == "19":
        print("\nChatbot: Thank you for using the ITC245 FAQ Chatbot. Goodbye!")
        break

    else:
        print("\nChatbot: Invalid choice. Please enter a number between 1 and 19.")

from student import Student
from professor import Professor
from course import Course
from registration import Registration
from storage import save_students, load_students

from storage import save_registrations, load_registrations

registration_data = [
    {
        "student_id": 101,
        "course_id": "CSE101",
        "status": "Registered"
    }
]

save_registrations(registration_data)
print("Saved registrations:", load_registrations())








student_data = [
    {
        "student_id": 101,
        "name": "Arun",
        "department": "CSE",
        "email": "arun@gmail.com"
    }
]

save_students(student_data)
print("Saved students:", load_students())






# Create a student
student = Student(101, "Arun", "CSE", "arun@gmail.com")

# Create a professor
professor = Professor(1, "John", "CSE")

# Create a course
course = Course("CSE101", "Python", 30)

# Display details
print("=== STUDENT DETAILS ===")
student.display_info()

print("\n=== PROFESSOR DETAILS ===")
professor.display_info()

print("\n=== COURSE DETAILS ===")
course.display_info()

# Register the student
print("\n=== REGISTRATION DETAILS ===")
registration = Registration(student, course)
registration.display_info()

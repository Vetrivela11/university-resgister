class Student:
    def __init__(self, student_id, name, department, email):
            self.student_id = student_id
            self.name = name
            self.department = department
            self.email = email

    def display_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Email:", self.email)


class Course:
    def __init__(self,course_id,course_name,max_students):
        self.course_id = course_id
        self.course_name = course_name
        self.max_students = max_students

    def display_info(self):
        print("Course ID:",self.course_id)
        print("Course Name:",self.course_name)
        print("Maximum Students:",self.max_students)
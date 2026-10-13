
class Professor:
    def __init__(self, professor_id, name, department):
        self.professor_id = professor_id
        self.name = name
        self.department = department

    def display_info(self):
        print("Professor ID:", self.professor_id)
        print("Name:", self.name)
        print("Department:", self.department)

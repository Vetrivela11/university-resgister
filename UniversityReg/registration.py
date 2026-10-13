
from exception import (
    StudentNOtFoundError,
    CourseNotFoundError,
    CourseFullError,
    AlreadyRegisteredError
)


class Registration:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.status = "Registered"

    def display_info(self):
        print("Student:", self.student.name)
        print("Course:", self.course.course_name)
        print("Status:", self.status)


def register_student(student, course, registrations):
    if student is None:
        raise StudentNOtFoundError("Student not found")

    if course is None:
        raise CourseNotFoundError("Course not found")

    for item in registrations:
        if (
            item["student_id"] == str(student.student_id)
            and item["course_id"] == str(course.course_id)
        ):
            raise AlreadyRegisteredError(
                "Student is already registered"
            )

    if len([
        item for item in registrations
        if item["course_id"] == str(course.course_id)
    ]) >= course.max_students:
        raise CourseFullError("Course is full")

    new_registration = Registration(student, course)

    registrations.append({
        "student_id": str(student.student_id),
        "course_id": str(course.course_id),
        "status": new_registration.status
    })

    return new_registration


import pytest

from student import Student
from course import Course
from registration import register_student
from exception import (
    CourseFullError,
    AlreadyRegisteredError,
    StudentNOtFoundError,
    CourseNotFoundError
)


def create_data():
    student = Student(101, "Arun", "CSE", "arun@gmail.com")
    course = Course("CSE101", "Python", 2)
    return student, course


def test_successful_registration():
    student, course = create_data()
    registrations = []

    result = register_student(student, course, registrations)

    assert result.status == "Registered"
    assert len(registrations) == 1


def test_duplicate_registration():
    student, course = create_data()
    registrations = []

    register_student(student, course, registrations)

    with pytest.raises(AlreadyRegisteredError):
        register_student(student, course, registrations)


def test_course_full():
    student, course = create_data()
    course.max_students = 1

    registrations = [
        {"student_id": "102", "course_id": "CSE101",
         "status": "Registered"}
    ]

    with pytest.raises(CourseFullError):
        register_student(student, course, registrations)


def test_student_not_found():
    _, course = create_data()

    with pytest.raises(StudentNOtFoundError):
        register_student(None, course, [])


def test_course_not_found():
    student, _ = create_data()

    with pytest.raises(CourseNotFoundError):
        register_student(student, None, [])

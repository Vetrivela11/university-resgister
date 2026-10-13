
from storage import (
    save_students,
    load_students,
    save_registrations,
    load_registrations,
)


def test_student_json_storage():
    students = [
        {
            "student_id": 101,
            "name": "Arun",
            "department": "CSE",
            "email": "arun@gmail.com",
        }
    ]

    save_students(students)
    assert load_students() == students


def test_registration_csv_storage():
    registrations = [
        {
            "student_id": "101",
            "course_id": "CSE101",
            "status": "Registered",
        }
    ]

    save_registrations(registrations)
    assert load_registrations() == registrations

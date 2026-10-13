
from student import Student


def test_student_details():
    student = Student(
        101,
        "Arun",
        "CSE",
        "arun@gmail.com"
    )

    assert student.student_id == 101
    assert student.name == "Arun"
    assert student.department == "CSE"
    assert student.email == "arun@gmail.com"


def test_student_display_info(capsys):
    student = Student(
        101,
        "Arun",
        "CSE",
        "arun@gmail.com"
    )

    student.display_info()
    output = capsys.readouterr().out

    assert "Student ID: 101" in output
    assert "Name: Arun" in output
    assert "Department: CSE" in output
    assert "Email: arun@gmail.com" in output

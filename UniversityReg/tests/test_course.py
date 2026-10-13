
from course import Course


def test_course_details():
    course = Course("CSE101", "Python", 30)

    assert course.course_id == "CSE101"
    assert course.course_name == "Python"
    assert course.max_students == 30


def test_course_display_info(capsys):
    course = Course("CSE101", "Python", 30)
    course.display_info()

    output = capsys.readouterr().out

    assert "Course ID: CSE101" in output
    assert "Course Name: Python" in output
    assert "Maximum Students: 30" in output

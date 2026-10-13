
from professor import Professor


def test_professor_details():
    professor = Professor(1, "John", "CSE")

    assert professor.professor_id == 1
    assert professor.name == "John"
    assert professor.department == "CSE"


def test_professor_display_info(capsys):
    professor = Professor(1, "John", "CSE")
    professor.display_info()

    output = capsys.readouterr().out

    assert "Professor ID: 1" in output
    assert "Name: John" in output
    assert "Department: CSE" in output

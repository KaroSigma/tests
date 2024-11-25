import os
from student import Student
from presence import Attendance

def cleanup(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def test_export_students():
    # GIVEN
    Student.list_of_students = []
    Student.add("Katarzyna", "Lewandowska")
    Student.add("Piotr", "Zieliński")

    # WHEN
    file_name = "students_export.csv"
    Student.save_to_file(file_name)

    # THEN
    assert os.path.exists(file_name)
    with open(file_name, "r") as f:
        content = f.read()
    assert content == "0,Katarzyna,Lewandowska\n1,Piotr,Zieliński\n"

    cleanup(file_name)

def test_import_students():
    # GIVEN
    file_name = "students_import.csv"
    with open(file_name, "w") as f:
        f.write("0,Katarzyna,Lewandowska\n1,Piotr,Zieliński\n")

    # WHEN
    Student.list_of_students = []
    Student.load_from_file(file_name)

    # THEN
    assert len(Student.list_of_students) == 2
    assert Student.list_of_students[0].first_name == "Katarzyna"
    assert Student.list_of_students[0].surname == "Lewandowska"
    assert Student.list_of_students[1].first_name == "Piotr"
    assert Student.list_of_students[1].surname == "Zieliński"

    cleanup(file_name)

def test_student_creation():
    # GIVEN:
    Student.list_of_students = []

    # WHEN:
    Student.add("Magdalena", "Wiśniewska")

    # THEN:
    assert len(Student.list_of_students) == 1
    assert Student.list_of_students[0].first_name == "Magdalena"
    assert Student.list_of_students[0].surname == "Wiśniewska"

def test_attendance_file_operations():
    # GIVEN:
    data = [
        {"id": 0, "status": True},
        {"id": 1, "status": False},
    ]
    attendance = Attendance("2024-12-25", data)
    file_name = "attendance_record.csv"

    # WHEN:
    attendance.save_to_file(file_name)

    # THEN:
    assert os.path.exists(file_name)

    # AND WHEN
    loaded_attendance = Attendance.load_attendance_from_file(file_name)

    # THEN:
    assert loaded_attendance.date == "2024-12-25"
    assert loaded_attendance.students_attendance == data

    cleanup(file_name)

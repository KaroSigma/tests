import pytest
import csv
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
    # GIVEN
    Student.list_of_students = []

    # WHEN
    Student.add("Magdalena", "Wiśniewska")

    # THEN
    assert len(Student.list_of_students) == 1
    assert Student.list_of_students[0].first_name == "Magdalena"
    assert Student.list_of_students[0].surname == "Wiśniewska"

def test_attendance_save_and_load():
    # GIVEN
    test_attendance_data = [
        {'id': 0, 'status': 1},
        {'id': 1, 'status': 0},
        {'id': 2, 'status': 1},
    ]
    file_name = "2024-10-30.csv"
    attendance = Attendance("2024-10-30", test_attendance_data)

    # WHEN
    attendance.save_to_file(file_name)

    # THEN
    assert os.path.exists(file_name)

    # WHEN
    loaded_attendance = Attendance.load_attendance_from_file(file_name)

    # THEN
    assert loaded_attendance is not None
    assert loaded_attendance.date == "2024-10-30", f"Niepoprawna data obecności: {loaded_attendance.date}"

    # THEN
    for original, loaded in zip(test_attendance_data, loaded_attendance.students_attendance):
        assert original['id'] == loaded['id'], f"ID studenta nie zgadza się: {original['id']} != {loaded['id']}"
        assert original['status'] == loaded['status'], \
            f"Status obecności nie zgadza się dla studenta {original['id']}: {original['status']} != {loaded['status']}"

    cleanup(file_name)

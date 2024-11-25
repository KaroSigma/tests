import os
import csv
from student import Student

# Adding a student
def add_student():
    print("Jeśli chcesz zakończyć działanie programu wpisz 'exit'")

    while True:
        name = input("Podaj imię studenta: ")
        if name.lower() == 'exit':
            break
        surname = input("Podaj nazwisko studenta: ")
        if surname.lower() == 'exit':
            break

        # Adding a student to the list
        Student.add(name, surname)
        print("Student został dodany.")

# Students update
def edit_students():
    if not Student.list_of_students:
        print("Brak studentów. Dodaj najpierw studenta.")
        return

    # Display students
    for idx, student in enumerate(Student.list_of_students):
        print(f"{idx}: {student.id} - {student.first_name} - {student.surname}")

    try:
        number = int(input("Podaj numer studenta do edytowania: "))
        if 0 <= number < len(Student.list_of_students):
            student = Student.get(number)
            name = input(f"Podaj nowe imię (aktualne: {student.first_name}): ") or student.first_name
            surname = input(f"Podaj nowe nazwisko (aktualne: {student.surname}): ") or student.surname

            # Update student data
            student.first_name = name
            student.surname = surname

            print("Dane studenta zostały zaaktualizowane.")
        else:
            print("Nieprawidłowy numer studenta.")
    except ValueError:
        print("Wprowadzony numer jest nieprawidłowy.")
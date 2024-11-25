from student import Student
from presence import Attendance
from adding_students import add_student, edit_students
from check_attendance import CheckAttendance
import os

class Main:
    def display_options():
        os.system('clear')
        print("[1] Obecność.")
        print("[2] Dodaj nowego studenta.")
        print("[3] Zaktualizuj studentów.")
        print("[4] Zapisz studentów.")
        print("[0] Wyjdź z interfejsu.")

    def menu():
        Main.display_options()
        option = int(input("Wprowadź opcję: "))

        while option != 0:
            if option == 1:
                CheckAttendance.menu()
            elif option == 2:
                add_student()
            elif option == 3:
                edit_students()
            elif option == 4:
                Student.save_to_file("students.csv")  # Save students to file
                print("Studenci zostali zapisani do pliku.")
            else:
                print("Wybrałeś złą opcję.")
            Main.display_options()
            option = int(input("Wprowadź opcję: "))
            print()
        print("Intefejs zakończył swoją pracę.")
        return

if __name__ == "__main__":
    Student.load_from_file("students.csv")
    Main.menu()
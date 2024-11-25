import os
from presence import Attendance
from student import Student
from datetime import datetime

if not os.path.exists('attendance'):
    os.makedirs('attendance')

class CheckAttendance:
    # Zwraca wszystkie pliki z obecnościami
    @staticmethod
    def get_all_attendance_files():
        files = [f for f in os.listdir("attendance/") if f.endswith('.csv')]
        return files

    # Tworzy nowy obiekt obecności dla wybranego dnia
    @staticmethod
    def create(filename):
        attendance_data = []
    
        # Przechodzi przez każdego studenta i zbiera informacje o obecności
        for s in Student.list_of_students:
            obecny = input(f"Czy {s.first_name} {s.surname} jest obecny? (wpisz 1 dla obecny, 0 dla nieobecny): ").strip()
            while obecny not in ["0", "1"]:
                obecny = input("Nieprawidłowa wartość. Wpisz 1 (obecny) lub 0 (nieobecny): ").strip()
            attendance_data.append({'id': s.id, 'status': int(obecny)})  # status zapisany jako 1 lub 0
        
        # Tworzy obiekt Attendance i zapisuje go do pliku
        attendance = Attendance(filename, attendance_data)
        attendance.save_to_file(f"attendance/{filename}.csv")

    # Umożliwia edycję obecności dla wybranego dnia
    @staticmethod
    def update(filename):
        attendance = Attendance.load_attendance_from_file(f"attendance/{filename}")
        
        if attendance:
            print(f"Data obecności: {attendance.date}")
            for record in attendance.students_attendance:
                student = Student.get(record['id'])
                obecny = input(f"Aktualizuj obecność dla {student.first_name} {student.surname} (aktualny status: {record['status']}). Wpisz 1 (obecny) lub 0 (nieobecny): ").strip()
                while obecny not in ["0", "1"]:
                    obecny = input("Nieprawidłowa wartość. Wpisz 1 (obecny) lub 0 (nieobecny): ").strip()
                record['status'] = int(obecny)  # aktualizacja statusu

            # Zapisujemy zmiany
            attendance.save_to_file(f"attendance/{filename}")

    def menu():
        attendance_files = CheckAttendance.get_all_attendance_files()
 
        print("\n\n")
        print("[1] Sprawdź obecność na dzień dzisiejszy")
        if len(attendance_files) != 0:
            print("[2] Edytuj poprzednie obecności")
        print("[0] Cofnij się")
        user_input = int(input("Wybierz: "))
        while user_input not in [1, 2, 0] or (user_input == 2 and len(attendance_files) == 0):
            user_input = int(input("Wybierz: "))

        if user_input == 0:
            return
        elif user_input == 1:
            date = datetime.now().strftime('%Y-%m-%d')
            CheckAttendance.create(date)
        elif user_input == 2:
            for index, a in enumerate(attendance_files):
                print(f"[{index}] {a}")
            
            file_index_input = int(input("Wybierz plik do edycji"))
            CheckAttendance.update(attendance_files[file_index_input])

if __name__ == "__main__":
    Student.load_from_file("students.csv")
    all_files = CheckAttendance.get_all_attendance_files()
    
    if all_files:
        CheckAttendance.update(all_files[0])
    else:
        filename = input("Podaj nazwę pliku dla nowej listy obecności (np. 2024-10-30): ")
        CheckAttendance.create(filename)

import csv
from datetime import date
import os

class Student:
    list_of_students = []
    def __init__(self, id, first_name, surname):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.obecnosci = {} 
        Student.list_of_students.append(self)

    # Returning student object when student exists
    @classmethod
    def get(cls, id):
        for s in cls.list_of_students:
            if int(s.id) == int(id):
                return s
        return None

    # Get next free id
    @classmethod
    def get_id(cls):
        try:
            return int(cls.list_of_students[-1].id) + 1
        except IndexError:
            return 0
    
    @staticmethod
    def add(first_name, surname):
        Student(Student.get_id(), first_name, surname)

    # This method is for reading data from file and create objects
    @classmethod
    def load_from_file(cls, file_name):
        if not os.path.isfile(file_name):
            return

        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                Student(row[0],row[1],row[2])

    # This method is for saving data from list_of_students to file
    @classmethod
    def save_to_file(cls, file_name):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            for person in Student.list_of_students:
                writer.writerow([person.id, person.first_name, person.surname])
    

    @classmethod
    def ogolnieobecnosc(cls, data):
        print(f"Sprawdzanie obecności na dzień: {data}")
        for student in cls.list_of_students:
            obecnosc = student.obecnosci.get(data)
            if obecnosc is not None:
                print(f"{student.first_name} {student.surname} - obecność JUZ BYLA wpisana:  {obecność}")
                nowa_obecnosc = input("Czy chcesz zaktualizować obecność? (tak/nie): ")
                if nowa_obecnosc.lower() == "tak":
                    obecnosc = input("Czy student jest obecny? Wpisz 1 gdy tak lub wpisz 0 gdy nie: ")
                    student.obecnosci[data] = int(obecnosc)
            else:
                obecnosc = input(f"Czy student {student.first_name} {student.surname} jest obecny? Wpisz 1 gdy tak lub wpisz 0 gdy nie: ")
                student.obecnosci[data] = int(obecnosc)

if __name__ == "__main__":
    Student(10, "Adam", "Nowak")
    print(Student.get(10).first_name)

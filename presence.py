import csv
from student import Student

class Attendance:
    def __init__(self, date, students_attendance):
        self.date = date
        self.students_attendance = students_attendance

    # Reading attendance from file (txt or csv) and returnin Attendance object
    @staticmethod
    def load_attendance_from_file(filename):
        date = filename[:-4]
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                return Attendance(date, [{'id':int(row[0]), 'status':bool(int(row[1]))} for row in reader])
        except FileNotFoundError:
            return None
        
    def save_to_file(self, filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for student in self.students_attendance:
                writer.writerow([student['id'], student['status']])


if __name__ == "__main__":
    test_attendance = Attendance("30-10-2024", [{'id':0, 'status':True}, {'id':1, 'status':True}, {'id':2, 'status':False}, {'id':3, 'status':True}])

    print(test_attendance.date)                                         # Get date
    print(test_attendance.students_attendance)                          # List of all students status
    print(test_attendance.students_attendance[0].get('id', None))       # Get student id
    print(test_attendance.students_attendance[0].get('status', None))   # Get student attendance status
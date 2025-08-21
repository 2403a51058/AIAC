
class Student:
    def __init__(self, name, age, student_id, marks):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Marks: {self.marks}")

    def display_student_grades(self):
        if self.marks < 0 or self.marks > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            return
        if self.marks >= 90:
            print(f"Grade: A")
        elif self.marks >= 75:
            print(f"Grade: B")
        elif self.marks >= 60:
            print(f"Grade: C")
        else:
            print(f"Grade: F")

    def display_student_info(self):
        self.display_info()
        self.display_student_grades()

students=[]
num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    name=input("Enter student's name: ")
    age=int(input("Enter student's age: "))
    student_id=input("Enter student's ID: ")
    marks=float(input("Enter student's marks: "))
    student=Student(name, age, student_id, marks)
    students.append(student)
    

for student in students:
    
    student.display_student_info()
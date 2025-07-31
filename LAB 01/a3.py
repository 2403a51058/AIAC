class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.course = input("Enter course: ")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Course: {self.course}")

# Example usage
student = Student()
student.display()
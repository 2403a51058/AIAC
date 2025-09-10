
# Refactored and optimised code

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

    def print_info(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp1.increase_salary(10)
    emp1.print_info()
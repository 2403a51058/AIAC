# Define the sru_student class
class sru_student:
    # Initialize the student object with name, roll no., and hostel status
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Store the student's name
        self.roll_no = roll_no  # Store the student's roll number
        self.hostel_status = hostel_status  # Store hostel status (Yes/No)
        self.fee_paid = False  # Track if fee is paid, default is False
    # Method to update the fee status
    def fee_update(self, status):
        self.fee_paid = status  # Update fee status (True/False)

    # Method to display student details
    def display_details(self):
        # Print all details of the student
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")


# Example usage:
# Create a student object
student1 = sru_student("Alice", "SRU123", "Yes")
# Update fee status
student1.fee_update(True)
# Display student details
student1.display_details()
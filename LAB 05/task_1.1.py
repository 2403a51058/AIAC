def collect_user_data():
    """Collect user data from input."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    return {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone,
        "address": address
    }

def save_data_to_file(filename, data):
    """Save user data to a .txt file."""
    with open(filename, "w") as f:
        for key, value in data.items():
            f.write(f"{key.capitalize()}: {value}\n")

def main():
    print("User Data Collection")
    user_data = collect_user_data()
    filename = input("Enter filename to save your data (e.g., data.txt): ")
    if not filename.endswith('.txt'):
        filename += '.txt'
    save_data_to_file(filename, user_data)
    print(f"Your data has been saved to {filename}.")

if __name__ == "__main__":
    main()

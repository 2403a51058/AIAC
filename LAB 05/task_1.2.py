import getpass
import hashlib

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

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

def anonymize_data(data):
    """Anonymize sensitive fields (simple masking)."""
    # Mask email and phone for privacy
    masked_email = data["email"][0] + "***@" + data["email"].split("@")[-1]
    masked_phone = "***" + data["phone"][-3:]
    return {
        "name": data["name"],
        "age": data["age"],
        "email": masked_email,
        "phone": masked_phone,
        "address": data["address"]
    }

def save_data_to_file(filename, password_hash, data):
    """Save password hash and anonymized data to a file."""
    with open(filename, "w") as f:
        # Store password hash at the top of the file
        f.write(f"PasswordHash:{password_hash}\n")
        # Write anonymized user data
        for key, value in data.items():
            f.write(f"{key.capitalize()}: {value}\n")

def main():
    print("User Data Collection")
    # Prompt user to create a password for protecting the file
    password = getpass.getpass("Create a password to protect your data file: ")
    password_hash = hash_password(password)
    # Collect user data
    user_data = collect_user_data()
    # Anonymize sensitive data
    anonymized_data = anonymize_data(user_data)
    # Save to file
    filename = input("Enter filename to save your data (e.g., data.txt): ")
    save_data_to_file(filename, password_hash, anonymized_data)
    print(f"Your anonymized data has been saved to {filename} and protected with your password.")

if __name__ == "__main__":
    main()

def generate_email(name):
    parts = name.strip().split()
    if len(parts) < 2:
        return None  # Invalid name format
    first_letter = parts[0][0].lower()
    last_name = parts[-1].lower()
    return f"{first_letter}{last_name}@sru.edu.in"

# Read student names from console
names = input("Enter student names separated by commas: ").split(',')

for name in names:
    email = generate_email(name)
    if email:
        print(email)
    else:
        print(f"Invalid name format: {name.strip()}")
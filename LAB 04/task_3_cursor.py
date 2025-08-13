def format_full_name():
    full_name = input("Enter full name: ").strip()
    parts = full_name.split()
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
        print(f"{last} , {first}")
    else:
        print("Please enter both first and last name.")

if __name__ == "__main__":
    format_full_name()

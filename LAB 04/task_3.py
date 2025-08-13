def format_name():
    full_name = input("Enter full name (First Last): ").strip()
    parts = full_name.split()
    if len(parts) != 2:
        print("Please enter a name in 'First Last' format.")
        return
    first, last = parts
    print(f"{last} , {first}")

if __name__ == "__main__":
    format_name()
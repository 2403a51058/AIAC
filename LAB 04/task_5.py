def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    num_lines = count_lines_in_file(filename)
    if num_lines is not None:
        print(f"Number of lines : {num_lines}")
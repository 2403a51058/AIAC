def process_scores(scores):
    if not scores:
        return None
    # Single-pass computation using built-ins for clarity and speed
    total = 0.0
    highest = scores[0]
    lowest = scores[0]
    count = 0
    for s in scores:
        count += 1
        total += s
        if s > highest:
            highest = s
        if s < lowest:
            lowest = s
    avg = total / count
    return (avg, highest, lowest)
if __name__ == "__main__":
    raw = input("Enter scores separated by spaces: ").strip()
    nums = []
    if raw:
        try:
            nums = [float(x) for x in raw.split()]
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    result = process_scores(nums)
    if result is None:
        print("No scores provided.")
    else:
        avg, highest, lowest = result
        print("Average:", avg)
        print("Highest:", highest)
        print("Lowest:", lowest)

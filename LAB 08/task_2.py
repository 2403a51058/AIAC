def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid input"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    score_input = input("Enter the score: ")
    try:
        score_value = float(score_input)
    except ValueError:
        score_value = score_input  # Pass invalid input to assign_grade
    print(assign_grade(score_value))

if __name__ == "__main__":
    main()


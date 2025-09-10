def grade(score):
    grades = ["F", "D", "C", "B", "A"]
    return grades[min(max(score // 10 - 5, 0), 4)]

# Example usage
scores = [95, 85, 75, 65, 55]
for s in scores:
    print(f"Score: {s}, Grade: {grade(s)}")
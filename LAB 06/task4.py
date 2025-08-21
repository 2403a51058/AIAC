print("sum of n natural numbers")

def sum(n):
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 1
    return total

num = int(input("Enter a number: "))

print(f"The sum of first {num} natural numbers is: {sum(num)}")
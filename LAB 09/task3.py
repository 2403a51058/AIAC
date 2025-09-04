def add(a, b):
    """
    This module provides basic arithmetic operations: addition, subtraction, multiplication, and division.
    Functions:
        add(a, b): Returns the sum of a and b.
        subtract(a, b): Returns the difference of a and b.
        multiply(a, b): Returns the product of a and b.
        divide(a, b): Returns the quotient of a divided by b. Raises ValueError if b is zero.
    Example usage:
    """
    return a + b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
# Example usage
if __name__ == "__main__":
    x = 10
    y = 5
    print("Add:", add(x, y))
    print("Subtract:", subtract(x, y))
    print("Multiply:", multiply(x, y))
    print("Divide:", divide(x, y))
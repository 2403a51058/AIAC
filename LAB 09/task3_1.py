def add(a, b):
    """
    Add two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The sum of a and b.
    """
    """
    Subtract the second number from the first number.
    Args:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.
    Returns:
        int or float: The result of a - b.
    """
    """
    Multiply two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The product of a and b.
    """
    """
    Divide the first number by the second number.
    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.
    Returns:
        float: The result of a divided by b.
    Raises:
        ValueError: If b is zero.
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

if __name__ == "__main__":
    x = 10
    y = 5
    print("Add:", add(x, y))
    print("Subtract:", subtract(x, y))
    print("Multiply:", multiply(x, y))
    print("Divide:", divide(x, y))
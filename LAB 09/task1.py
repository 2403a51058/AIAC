"""Utilities to split a list of integers into even and odd numbers.

This module exposes a reusable function `split_even_and_odd` and a simple
`main` entry point that demonstrates its use by printing the results.
"""
def split_even_and_odd(numbers):
    """Split integers into even and odd lists.

    Args:
        numbers: Iterable of integers to classify by parity.

    Returns:
        A tuple (even_numbers, odd_numbers), each a list of integers.
    """
    even_numbers=[]
    odd_numbers=[]
    for number in numbers:
        if number%2==0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers
def main():
    """Demonstrate splitting and print even/odd lists for a sample input."""
    numbers=[1,2,3,4,5,66,45,34,23,12,6,54,98,68,90,43,33,51]
    even_numbers, odd_numbers = split_even_and_odd(numbers)
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)


if __name__ == "__main__":
    main()

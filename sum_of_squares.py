def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.
    
    Args:
        numbers (list): A list of numbers (int or float)
    
    Returns:
        int or float: The sum of squares of all numbers in the list
    
    Example:
        >>> sum_of_squares([1, 2, 3, 4])
        30
        >>> sum_of_squares([2.5, 3.5])
        18.5
        >>> sum_of_squares([])
        0
    """
    if not numbers:
        return 0
    
    return sum(num ** 2 for num in numbers)


# Example usage and test cases
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4],      # Expected: 1 + 4 + 9 + 16 = 30
        [2.5, 3.5],        # Expected: 6.25 + 12.25 = 18.5
        [],                # Expected: 0
        [5],               # Expected: 25
        [-2, -3, 4]        # Expected: 4 + 9 + 16 = 29
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        result = sum_of_squares(test_case)
        print(f"Test {i}: sum_of_squares({test_case}) = {result}")
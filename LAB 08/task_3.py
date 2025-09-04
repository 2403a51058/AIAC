# Test cases for is_sentence_palindrome(sentence)
test_cases = [
    # (Input sentence, Expected output)
    ("A man, a plan, a canal: Panama", True),
    ("No lemon, no melon", True),
    ("Was it a car or a cat I saw?", True),
    ("", True),  # Edge case: empty string
    ("a", True),  # Edge case: single character
    ("Hello, World!", False),
    ("Eva, can I see bees in a cave?", True),
    ("Never odd or even.", True),
    ("This is not a palindrome", False),
    ("12321", True),  # Numeric palindrome
    ("12345", False),  # Numeric non-palindrome
    ("Able was I, ere I saw Elba!", True),
    ("Step on no pets", True),
    ("Top spot", True),
    ("Palindrome", False),
]

def is_sentence_palindrome(sentence):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Run test cases
    print("Running test cases for is_sentence_palindrome:")
    for idx, (input_sentence, expected) in enumerate(test_cases, 1):
        result = is_sentence_palindrome(input_sentence)
        print(f"Test case {idx}: Input: {repr(input_sentence)} | Expected: {expected} | Got: {result} | {'PASS' if result == expected else 'FAIL'}")

    # Take input from the user and check palindrome
    user_input = input("Enter a sentence to check if it's a palindrome: ")
    if is_sentence_palindrome(user_input):
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")

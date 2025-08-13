def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    num_vowels = count_vowels(user_input)
    print(f"Number of vowels  : {num_vowels}")
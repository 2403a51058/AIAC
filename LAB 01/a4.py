def word_frequency(text):
    freq = {}
    words = text.split()
    for word in words:
        word = word.lower().strip('.,!?;:"()[]{}')
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage
sample_text = "This is a test. This test is only a test."
print(word_frequency(sample_text))
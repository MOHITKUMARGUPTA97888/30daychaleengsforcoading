def filter_long_words(word_list, length):
    result = [word for word in word_list if len(word) > length]
    return result

# Example usage:
words = ["apple", "banana", "cherry", "date"]
long_words = filter_long_words(words, 5)
print(long_words)  # Output: ["banana", "cherry"]

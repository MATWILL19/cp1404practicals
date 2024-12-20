"""
Word Occurrences
Estimate: 30 minutes
Actual:   50 minutes
"""
word_to_count = {}

word_input = input("Please enter a sentence: ")
words = word_input.split(" ")
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
words = list(word_to_count.keys())
words.sort()
word_length = max((len(word) for word in word_input))
for word in words:
    print(f"{word:{word_length}} : {word_to_count[word]}")

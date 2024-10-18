"""
Word Occurrences
Estimate: 30 minutes
Actual:   32 minutes
"""
word_to_count = {}

words = input("Please enter a sentence: ")
parts = words.split(" ")
for part in parts:
    word_to_count[part] = word_to_count.get(part, 0) + 1
for word in word_to_count:
    width = 10
    print(f"{word:{width}} : {word_to_count[word]}")

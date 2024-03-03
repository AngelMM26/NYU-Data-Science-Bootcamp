# Write a function count_vowels(word) that takes a word as an argument and 
# returns the number of vowels in the word.

def count_vowels(word):
    count = 0
    for i in word:
        if i in ("a", "e", "i", "o", "u"):
            count += 1
    return count
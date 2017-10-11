import string
for _ in range(int(input())):
    missingLetters = list(string.ascii_lowercase)   # ['a', 'b', 'c', ..., 'z']
    phrase = input()
    print(phrase.lower())   # .lower() converts all uppercase to lowercase

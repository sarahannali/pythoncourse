def vowel_count(word):
    vowelDict = {}
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        letter = letter.lower()
        if letter in vowels:
            if letter not in vowelDict:
                vowelDict[letter] = 1
            else:
                vowelDict[letter] += 1
    return vowelDict
   

print(vowel_count('awesome'))  # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie'))  # {'e': 2, 'i': 1}
print(vowel_count('Colt'))  # {'o': 1}

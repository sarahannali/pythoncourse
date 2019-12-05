def reverse_vowels(givenString):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    stringVowels = []
    stringNoVowels = []
    for letter in givenString:
        if letter in vowels:
            stringVowels.append(letter)
            stringNoVowels.append("*")
        else:
            stringNoVowels.append(letter)
    stringVowels.reverse()
    num = 0
    for i,item in enumerate(stringNoVowels):
        if item == "*":
            stringNoVowels[i] = stringVowels[num]
            num += 1
    return "".join(stringNoVowels)

print(reverse_vowels("Hello!")) # "Holle!" 
print(reverse_vowels("Tomatoes")) # "Temotaos" 
print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou")) # "uoiea"
print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"
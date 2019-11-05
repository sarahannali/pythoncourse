word = input("Input a word and will return if palindrome: ")

def reverseString(x):
    return x[::-1].replace(" ", "").upper()

def isPalindrome(string):
    if reverseString(string) == string.replace(" ", "").upper():
        return True
    return False

reverseString(word)
print(isPalindrome(word))
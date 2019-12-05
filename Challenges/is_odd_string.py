def is_odd_string(givenString):
    letters = list(map(chr,range(97,123)))
    numbers = [num for num in range(1,27)]
    letterDict = dict(zip(letters,numbers))
    ans = 0
    for letter in givenString:
        ans += letterDict[letter]
    if ans%2 == 0:
        return False
    return True

print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False
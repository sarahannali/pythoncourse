def dict_creation(number):
    numDict = {}
    for digit in str(number):
        if digit in numDict:
            numDict[digit] += 1
        if digit not in numDict:
            numDict[digit] = 1
    return numDict

def same_frequency(numOne,numTwo):
    ansOne = dict_creation(numOne)
    ansTwo = dict_creation(numTwo)
    if ansOne == ansTwo:
        return True
    return False

print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True
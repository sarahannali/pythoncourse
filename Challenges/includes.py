def checkGiven(givenList,givenNum,givenIndex):
    newList = [x for x in givenList if givenList.index(x)>=givenIndex]
    if givenNum in newList:
        return True
    return False

def includes(given, givenNum, givenIndex=0):
    if type(given) == str:
        givenList = [x for x in given]
    if type(given) == list:
        givenList = given
    if type(given) == dict:
        givenList = [x for x in given.values()]
    return checkGiven(givenList,givenNum,givenIndex)

print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False
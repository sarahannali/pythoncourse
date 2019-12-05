'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

def mode(givenList):
    numDict = {}
    for num in givenList:
        if num in numDict:
            numDict[num] += 1
        if num not in numDict:
            numDict[num] = 1
    finalAns = max(numDict,key=numDict.get)
    return finalAns

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

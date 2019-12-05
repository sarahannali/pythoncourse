def find_the_duplicate(givenList):
    numDict = {}
    finalAns = None
    for num in givenList:
        if num in numDict:
            numDict[num] += 1
        if num not in numDict:
            numDict[num] = 1
        ans = numDict[num]
        if ans >= 2:
            finalAns = num
    return finalAns

print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None

def sum_pairs(givenList, summation):
    listLen = len(givenList)-1
    usedNums = []
    for num in range(0,listLen):
        for item in givenList:
            if (givenList.index(item) != num) and (item not in usedNums):
                ans = item + givenList[num]
                if ans == summation:
                    return [givenList[num],item]
        usedNums.append(givenList[num])
    return []

print(sum_pairs([4,2,10,5,1,10],6))
print(sum_pairs([11,20,4,2,1,5], 100)) # []
def two_oldest_ages(givenList):
    givenList.sort()
    return [givenList[len(givenList)-2],givenList[len(givenList)-1]]

print(two_oldest_ages( [1, 2, 10, 8] )) # [8, 10]
print(two_oldest_ages( [6,1,9,10,4] )) # [9,10]
print(two_oldest_ages( [4,25,3,20,19,5] )) # [20,25]
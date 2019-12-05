def find_greater_numbers(givenList):
    ans = 0
    for num in givenList:
        for x in range(givenList.index(num)+1,len(givenList)):
            if givenList[x] <= num:
                pass
            else:
                ans += 1
    return ans

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0
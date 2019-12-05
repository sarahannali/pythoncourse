def range_in_list(givenList,start=0,end=None):
    ans = 0
    if end == None:
        end = len(givenList)
    elif end > len(givenList):
        end = len(givenList)
    else:
        end = end + 1
    for x in range(start,end):
        ans += givenList[x]
    return ans

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0
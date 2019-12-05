def three_odd_numbers(givenList):
    for i in range(0,len(givenList)-2):
        ans = givenList[i] + givenList [i+1] + givenList[i+2]
        if ans%2 != 0:
            return True
    return False

print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False

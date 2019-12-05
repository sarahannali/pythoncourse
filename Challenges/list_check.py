def list_check(givenList):
    ans = 0
    for item in givenList:
        if type(item) != list:
            ans += 1
    if ans == 0:
        return True
    else:
        return False

print(list_check([[],[1],[2,3], (1,2)])) # False
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True
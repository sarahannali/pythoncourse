def remove_every_other(givenList):
    for item in givenList:
        indexofItem = givenList.index(item)
        if not indexofItem%2 == 0:
            givenList[indexofItem] = ""
    ansList = [i for i in givenList if i != ""]
    return ansList

print(remove_every_other([1,2,3,4,5])) # [1,3,5] 
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1])) # [1] 
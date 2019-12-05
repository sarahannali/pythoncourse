def two_list_dictionary(listOne, listTwo):
    dictAns = zip(listOne,listTwo)
    dictAns = dict(dictAns)
    if len(listOne) > len(listTwo):
        for x in range(len(listTwo),len(listOne)):
            dictAns[listOne[x]] = None
    return dictAns

print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z',]  , [1,2])) # {'x': 1, 'y': 2, 'z': None}

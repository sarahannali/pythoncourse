'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''

def sum_up_diagonals(givenArray):
    ans = 0
    for listItem in givenArray:
        listIndex = givenArray.index(listItem)
        x = listItem[listIndex]
        y = listItem[(len(listItem)-1)-listIndex]
        ans += x+y
    return ans

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1)) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
print(sum_up_diagonals(list2)) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

print(sum_up_diagonals(list3)) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
print(sum_up_diagonals(list4)) # 68
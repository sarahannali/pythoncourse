def find_factors(factor):
    factorsList = []
    for num in range(1,factor):
        if num not in factorsList:
            test = factor%num
            if test == 0:
                factorsList.append(num)
                factorsList.append(int(factor/num))
    factorsList.sort()
    return factorsList

print(find_factors(10)) # [1,2,5,10 ]
print(find_factors(11)) # [1,11]
print(find_factors(111)) # [1,3,37,111 ]
print(find_factors(321421)) # [1,293,1097,321421 ]
print(find_factors(412146)) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
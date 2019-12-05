'''
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''

def next_prime():
    num = 2
    allnums = []
    while True:
        for prime in allnums:
            if num % prime == 0:
                break
        else:
            allnums.append(num)
            yield num
        num += num%2 + 1

primes = next_prime()
print([next(primes) for i in range(5)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
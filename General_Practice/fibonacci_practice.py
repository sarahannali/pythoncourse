#Fibonacci Question

print("Fibonacci Sequence:")

def fib(length):
    a = 0
    b = 1
    count = 0
    while count < length:
        a, b = b, a+b
        yield a
        count += 1

for n in fib(5):
    print(n)

#Multiplier Question

print("Multiples:")

def getMultiples(startNum=1, count=10):
    currentCount = 1
    while currentCount <= count:
        yield (startNum*currentCount)
        currentCount += 1

for n in getMultiples(2,3):
    print(n)

print("Unlimited Multiples:")

def unlimitedMultiples(num=1):
    count = 1
    while True:
        yield num*count
        count += 1

sevens = unlimitedMultiples(7)
print([next(sevens) for i in range(15)])
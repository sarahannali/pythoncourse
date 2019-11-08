class Counter:
    def __init__(self,high):
        self.current = 0
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

def myFor(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            ans = next(iterator)
        except StopIteration:
            break
        else:
            func(ans)

def square(x):
    print(x*x)

myFor(Counter(5), square)
from time import time
from functools import wraps

def speedTest(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print(f"Executing {fn.__name__}")
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print (f"Time Elapsed: {t2-t1}")
        return f"Function Result: {result}"
    return wrapper

@speedTest
def genSum():
    return sum(x for x in range(50000000))

@speedTest
def listSum():
    return sum([x for x in range(50000000)])

print(genSum())
print(listSum())
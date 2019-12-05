def once(func):
    func.invoked = False
    def done(*args):
        if not func.invoked:
            func.invoked = True
            return func(*args)
    return done
    

def add(a,b):
    return a+b

oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None
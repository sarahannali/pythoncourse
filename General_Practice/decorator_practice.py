from functools import wraps
from time import sleep

def showArgs(fn):
    @wraps(fn)
    def wrapped(*args,**kwargs):
        print("Here are the args: {}".format(args))
        print("Here are the kwargs:{}".format(kwargs))
        return fn
    return wrapped

def delay(secs):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            print("Waiting {}s before running {}".format(secs, fn.__name__))
            sleep(secs)
            return fn(*args,**kwargs)
        return wrapper
    return inner

@delay(5)
@showArgs
def finalFunc(*args,**kwargs):
    pass

finalFunc(1,2,3,hello="goodbye")
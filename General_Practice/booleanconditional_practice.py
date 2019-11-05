import random

#Conditional Practice

x = random.randint(-100, 100)                               
while x == 0:             
    x = random.randint(-100, 100)                                
y = random.randint(-100, 100)                               
while y == 0:          
    y = random.randint(-100, 100)                           

if x > 0 and y > 0:
    print("both positive")
if x < 0 and y < 0:
    print("both negative")
if x > 0 and y < 0:
    print("x is positive and y is negative")
if x < 0 and y > 0:
    print("y is positive and x is negative")

#Boolean Practice

actuallySick = random.choice([True, False])
kindaSick = random.choice([True, False])
hateJob = random.choice([True, False])
sickDays = random.randint(0, 10)

callingSick = None

def callSick():
    if sickDays and actuallySick == True:
        callingSick = True
    elif sickDays and (kindaSick == True and hateJob == True):
        callingSick = True
    else:
        callingSick = False
    return callingSick

print(f"Will you call in sick? {callSick()}")
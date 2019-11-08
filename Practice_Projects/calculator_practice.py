floatChoice = input("Would you like to make your result a float? (Y/N) ").lower()

if floatChoice == "Y":
    ans1 = True
else:
    ans1 = False

ans2 = input("What operation would you like to use? (add, multiply, divide, subtract) ").lower()
ans3 = input("What's your first input? ")
ans4 = input("What's your second input? ")

def calculate(**kwargs):
    operations = {
        'add': (kwargs["first"] + kwargs["second"]),
        'multiply': (kwargs["first"] * kwargs["second"]),
        'divide': (kwargs["first"] / kwargs["second"]),
        'subtract': (kwargs["first"] - kwargs["second"])
    }

    getOperation = operations[kwargs.get('operation')]

    if kwargs.get('makeFloat') == False:
        return f"The answer is {int(getOperation)}"
    if kwargs.get('makeFloat') == True:
        return f"The answer is {float(getOperation)}"

print(calculate(makeFloat = ans1, operation = ans2, first = int(ans3), second = int(ans4)))
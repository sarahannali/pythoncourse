# #List Comprehension Practice

a = input("List 5 numbers less than 10, separated by a space: ")
b = input("List 5 more numbers less than 10: ")
a = a.replace(" ", "")

answer = [item for item in a and b if item in a and b] #Shared in both

inputOne = input("What is your name? ")
inputTwo = input("What is your pet's name? ")
inputThree = input("What is your favorite color? ")

listNames = [inputOne, inputTwo, inputThree]

answer2 = [name[::-1].lower() for name in listNames] #Reverse a string

print(f"\nYour number inputs shared the following numbers: {answer}")
print(f"\nThose words backward are {answer2}")

#Dictionary Practice

import random

options = ["pizza", "bread", "cookies", "cakes", "coffee"]

print(f"\nWELCOME! We sell {options}")
choice = input("What would you like to buy? ")

stock = {
    "pizza" : random.randint(1,10),
    "bread": random.randint(1,20),
    "cookies": random.randint(1,100),
    "cakes": random.randint(1,5),
    "coffee": random.randint(1,100)
}

amount = stock.get(choice)

if choice in stock:
    if amount > 1:
        choiceFix = choice + "s"
    else:
        choiceFix = choice
    print(f"\nWe have {amount} {choiceFix} left")
else:
    print("\nSorry, we don't make that!")
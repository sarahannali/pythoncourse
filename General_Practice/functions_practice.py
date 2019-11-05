aCreated = input("Create a list of numbers separated by spaces (ex: 1 2 3): ")
aList = list(map(str,aCreated.split()))

#List Manipulation

command = input("Would you like to add to or remove from this list? ")
location = input("Would you like to do this at the beginning or end of the list? ")

if command == "add":
    value = input("What number would you like to add? ")
else:
    value=None

def aList_manipulation(aList, command, location, value):
    if command == "remove":
        if location == "end":
            aList.pop()
            return f"Your new list is {aList}"
        if location == "beginning":
            aList.pop(0)
            return f"Your new list is {aList}"
    if command == "add":
        if location == "beginning":
            aList.insert(0, value)
            return f"Your new list is {aList}"
        if location == "end":
            aList.append(value)
            return f"Your new list is {aList}"

print(aList_manipulation(aList, command, location, value))

bCreated = input("\nCreate another list separated by spaces (ex: 1 2 3 or a b c): ")
bList = list(map(str,bCreated.split()))

def interleave (a,b):
    newZip = list(zip(a,b))
    newZip2 = list(x[0] + x[1] for x in newZip)
    return "".join(newZip2)

interwoven = interleave(aList,bList)

print(f"Your lists interwoven would be {interwoven}")
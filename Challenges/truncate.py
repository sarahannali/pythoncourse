def truncate(givenString,length):
    if length < 3:
        return "Truncation must be at least 3 characters."
    elif length > len(givenString):
        return givenString
    else:
        ans = ""
        for num in range(0,length-3):
            ans = ans + givenString[num]
        return ans + "..."


print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 1)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters."
print(truncate("Hello World", 6)) # "Hel..."
print(truncate("Problem solving is the best!", 10)) # "Problem..."
print(truncate("Another test", 12)) # "Another t..."
print(truncate("Woah", 4)) # "W..."
print(truncate("Woah", 3)) # "..."
print(truncate("Yo",100)) # "Yo"
print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"
def yes_or_no():
    choice = "yes"
    while True:
        yield choice
        if choice == "yes":
            choice = "no"
        else:
            choice = "yes"


gen = yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def make_song(num=99, beverage="soda"):
    for numbottles in range (num,-1,-1):
        if numbottles > 1:
            yield f"{numbottles} bottles of {beverage} on the walls"
        elif numbottles == 1:
            yield f"Only 1 bottle of {beverage} left!"
        else:
            yield f"No more {beverage} left!"

def_song = make_song(10,"milk")

print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
print(next(def_song))
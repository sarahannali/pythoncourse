import random

num = random.randint(1,100)
player = None

print("The computer has chosen a number between 1 and 100. Can you guess it?")

while True:
    player = int(input("Your guess: "))
    if player > num:
        print("Too high!")
    elif player < num:
        print("Too low!")
    else:
        print("You got it!")
        new = input("Would you like to play again? (Y/N) ").upper()
        if new == "Y":
            player = None
            num = random.randint(1,100)
            print("The computer has chosen a new number!")
        else:
            break
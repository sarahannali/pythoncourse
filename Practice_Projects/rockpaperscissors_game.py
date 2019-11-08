import random

print(f"ROCK!\n PAPER!\n  SCISSORS!\n")
gameNum = int(input("How many games would you like to play? "))
print("\n")

pWins = 0
cWins = 0

while pWins < gameNum and cWins < gameNum:
    player = input("Enter your choice: ").lower()
    allowed = ("rock", "paper", "scissors")
    while player not in allowed:
        print("That is not a valid input! Please try again.")
        player = input("Enter your choice: ").lower()
    computer = random.randint(0,2)
    if computer == 0:
        comp = "rock"
    elif computer == 1:
        comp = "paper"
    else:
        comp = "scissors"
    print(f"You played {player}. The computer played {comp}.")
    if player == comp:
        pWins += 1
        cWins += 1
        print(f"It's a tie! Player wins: {pWins} Computer wins: {cWins}")
    elif player == "rock" and comp == "scissors":
        pWins += 1
        print(f"You win! Player wins: {pWins} Computer wins: {cWins}")
    elif player == "paper" and comp == "rock":
        pWins += 1
        print(f"You win! Player wins: {pWins} Computer wins: {cWins}")
    elif player == "scissors" and comp == "rock":
        pWins += 1
        print(f"You win! Player wins: {pWins} Computer wins: {cWins}")
    else:
        cWins += 1
        print(f"You lost :( Player wins: {pWins} Computer wins: {cWins}")

if pWins == gameNum:
    print("\nYou won!")
else:
    print("\nThe computer won!")
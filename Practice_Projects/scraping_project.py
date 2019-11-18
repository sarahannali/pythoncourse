import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import json

url = "http://quotes.toscrape.com"
page = "/page/1/"

scraping = input("Do you need to re-scrape the website? (Y/N) ").upper()

if scraping == "Y":
    with open("scraping_project.json", "w") as File:
        allQuotes = []
        while page:
            response = requests.get(f"{url}{page}")
            print(f"now scraping {url}{page}...")
            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all(class_="quote")

            for quote in quotes:
                quotetxt = quote.find(class_="text").get_text(),
                authortxt = quote.find(class_="author").get_text()
                biolink = quote.find("a")["href"]
                allQuotes.append({
                    "quote": quotetxt,
                    "author": authortxt,
                    "biolink": biolink
                })

            nextButton = soup.find(class_="next")
            page = nextButton.find("a")["href"] if nextButton else None
            sleep(2)
        json.dump(allQuotes, File)
        scraping = "N"


def hintData(link,name):
    response = requests.get(f"{url}{link}")
    soup = BeautifulSoup(response.text, "html.parser")

    birthday = soup.find(class_="author-born-date").get_text()
    birthplace = soup.find(class_="author-born-location").get_text()
    firstInitial = name[0].upper()
    fullName = name.split()
    fullInitials = fullName[0][0].upper() + fullName[len(fullName)-1][0].upper()

    return [f"This person's full initials are {fullInitials}", f"This person's first name starts with {firstInitial}", f"This person was born on {birthday} {birthplace}"]

if scraping == "N":
    with open("scraping_project.json", "r") as File:  # fix so no special characters
        data = json.load(File)
        playerAns = None

        while True:
            if playerAns == None:
                quoteNum = randint(0,99)
                tryNum = 5
                hintNum = 3
                randQuote = data[quoteNum]["quote"]
                ans = data[quoteNum]["author"].upper()
                print(f"\nGuess who said this quote:\n{randQuote}\n")
                playerAns = input(f"You have {tryNum} tries. Your guess: ").upper()

            elif playerAns == ans:
                playAgain = input("\nYou got it! Would you like to play again? (Y/N) ").upper()
                if playAgain == "Y":
                    playerAns = None
                else:
                    break

            elif playerAns != ans and hintNum > 2:
                tryNum -= 1
                hintNum -= 1
                playerAns = input(f"\nTry again. You have {tryNum} tries left. Your guess: ").upper()
            
            elif playerAns != ans and 0 <= hintNum <= 2:
                tryNum -= 1
                hints = hintData(data[quoteNum]["biolink"],ans)
                playerAns = input(f"\nTry again. You have {tryNum} tries left. Here's a hint: {hints[hintNum]}. Your guess: ").upper()
                hintNum -= 1

            else:
                playAgain = input(f"\nYou lost :( The answer was {ans} Play again? (Y/N) ").upper()
                if playAgain == "Y":
                    playerAns = None
                else:
                    break
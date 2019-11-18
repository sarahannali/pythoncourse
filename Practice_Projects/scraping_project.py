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
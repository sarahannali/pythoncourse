import requests
import random

url = "https://www.icanhazdadjoke.com/search"

uinput = input("What would you like to hear a joke about? ")

res = requests.get(
    url,
    params={
        "term":uinput
    },
    headers={
        "Accept":"application/json"
    },
)

rjson = res.json()

ans = rjson["results"]

if not ans:
    print(f"Sorry! There are no jokes about {uinput}. Try again?")

else:
    jokenum = random.randint(0,(len(ans)-1))
    joke = ans[jokenum]['joke']
    print(joke)
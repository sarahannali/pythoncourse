import pyfiglet
import termcolor
import colorama

colorama.init()
allowed = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

message = input("what message do you want to print? ")

color = input("what color do you want it to be? ")

while color not in allowed:
    print(f"That is not a valid color! Please choose from this list: {allowed}")
    color = input("what color do you want it to be? ")

pyfig = pyfiglet.figlet_format(message)

result = termcolor.colored(pyfig, color)

print(result)
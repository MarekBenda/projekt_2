"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marek Benda
email: czechmarekbenda@gmail.com
"""
import random

hodnota = "" 
while len(hodnota) < 4:
    cislo = str(random.randint(0, 9)) 
    if len(hodnota) == 0 and cislo == "0": 
        continue
    if cislo not in hodnota: 
        hodnota += cislo

print(
    "Hi there!",
    "-" * 47,
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.",
    "-" * 47,
    sep="\n"
)

pokusy = 0 

print("Enter a number:")
print("-" * 47)

while True:
    hadani = input(">>> ")

    nevalidni = []  

    if not hadani.isdigit():
        nevalidni.append("Invalid input! The input must be numeric.")
    if len(hadani) != 4:
        nevalidni.append("Invalid input! The number ought to be a 4-digit one.")
    if hadani[0] == "0":
        nevalidni.append("Invalid input! The number cannot begin with a 0.")
    if len(set(hadani)) != len(hadani):
        nevalidni.append("Invalid input! The digits must be unique.")

    if nevalidni:
        for duvody in nevalidni:
            print(duvody)
        continue

    pokusy += 1

    bulls = 0
    cows = 0

    for i in range(4): 
        if hadani[i] == hodnota[i]:
            bulls += 1
        elif hadani[i] in hodnota:
            cows += 1

    if bulls == 4:
        print("Correct, you've guessed the right number")
        print(f"in {pokusy} guess{'es' if pokusy != 1 else ''}!")
        print("-" * 47)
        print("That's amazing!")
        break
    else:
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        print("-" * 47)

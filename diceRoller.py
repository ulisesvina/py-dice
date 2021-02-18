from random import random

def rollDice(mode):
    modeLowerCase = mode.lower()
    if(modeLowerCase == "abs"):
        print("Result: ", int((random() * 6) + 1))
    elif modeLowerCase == "avg":
        iterations = int(input("Max. number of iterations: "))
        x=0
        for i in range(0, iterations):
            x = x + int((random() * 6) + 1)
        print("Result:", int(x/iterations))
import sys
from diceRoller import *

args = sys.argv
del args[0]

def nullValue():
    print("Null value inputted. Execution will continue in 'abs' mode.")
    mode = "abs"

if len(args) == 0:
    mode = input("Mode (avg/abs): ")
    if len(mode) == 0:
        nullValue()
    rollDice(mode)
else:
    if len(args[0]) == 0:
        nullValue()
    rollDice(args[0])
import pyautogui
import pydirectinput
import re
import time

regexUp = "^haut[1-4]?$"
regexDown = "^bas[1-4]?$"
regexLeft = "^gauche[1-4]?$"
regexRight = "^droite[1-4]?$"
regexA = "^a[1-4]?$"
regexB = "^b[1-4]?$"
regexX = "^x[1-4]?$"
regexY = "^y[1-4]?$"

def isValidKeyRegex(message, regex):
    if(re.match(regex, message, re.IGNORECASE)) : 
        if message.isalpha():
            return 1
        else :
            return int(message[-1])
    else:
        return 0

def action(message):
    i=0
    while i < isValidKeyRegex(message, regexUp):
        print(isValidKeyRegex(message, regexUp))
        i+=1
    while i < isValidKeyRegex(message, regexDown):
        pydirectinput.press("down")
        i+=1
    while i < isValidKeyRegex(message, regexLeft):
        print("left")
        i+=1
    while i < isValidKeyRegex(message, regexRight):
        print("right")
        i+=1
    while i < isValidKeyRegex(message, regexX):
        print("s")
        i+=1
    while i < isValidKeyRegex(message, regexA):
        print("x")
        i+=1
    while i < isValidKeyRegex(message, regexB):
        print("z")
        i+=1
    while i < isValidKeyRegex(message, regexY):
        print("a")
        i+=1

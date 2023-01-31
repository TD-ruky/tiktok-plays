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
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0

def keyAction(message):
    i=0
    while i < isValidKeyRegex(message, regexUp):
        pydirectinput.press("up")
        i+=1
    while i < isValidKeyRegex(message, regexDown):
        pydirectinput.press("down")
        i+=1
    while i < isValidKeyRegex(message, regexLeft):
        pydirectinput.press("left")
        i+=1
    while i < isValidKeyRegex(message, regexRight):
        pydirectinput.press("right")
        i+=1
    while i < isValidKeyRegex(message, regexX):
        pydirectinput.press("s")
        i+=1
    while i < isValidKeyRegex(message, regexA):
        pydirectinput.press("x")
        i+=1
    while i < isValidKeyRegex(message, regexB):
        pydirectinput.press("z")
        i+=1
    while i < isValidKeyRegex(message, regexY):
        pydirectinput.press("a")
        i+=1

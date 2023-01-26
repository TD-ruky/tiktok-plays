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

def isUp(message):
    if(re.match(regexUp, message, re.IGNORECASE)) : 
        #if input is "haut" with no more indication
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0

def isDown(message):
    if(re.match(regexDown, message, re.IGNORECASE)) : 
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0

def isLeft(message):
    if(re.match(regexLeft, message, re.IGNORECASE)) : 
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0

def isRight(message):
    if(re.match(regexRight, message, re.IGNORECASE)) : 
        if isinstance(message, str):
            return 1
        else :
            print(message[-1])
            return message[-1]
    else:
        return 0
def isX(message):
    if(re.match(regexX, message, re.IGNORECASE)) : 
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0
def isY(message):
    if(re.match(regexY, message, re.IGNORECASE)) : 
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0
def isA(message):
    if(re.match(regexA, message, re.IGNORECASE)) : 
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0
def isB(message):
    if(re.match(regexB, message, re.IGNORECASE)) : 
        if isinstance(message, str):
            return 1
        else :
            return message[-1]
    else:
        return 0

def action(message):
    print()
    i=0
    while i < isUp(message):
        pydirectinput.press("up")
        i+=1
    while i < isDown(message):
        pydirectinput.press("down")
        i+=1
    while i < isLeft(message):
        pydirectinput.press("left")
        i+=1
    while i < isRight(message):
        pydirectinput.press("right")
        i+=1
    while i < isX(message):
        pydirectinput.press("s")
        i+=1
    while i < isA(message):
        pydirectinput.press("x")
        i+=1
    while i < isB(message):
        pydirectinput.press("z")
        i+=1
    while i < isY(message):
        pydirectinput.press("a")
        i+=1

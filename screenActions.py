import pyautogui
import win32api
import win32con
import re
import time
from appDimensions import get_active_app_name
from moveOnScreenTest import moveFromTo
from hexagon import hexagon

uselessHeight = 80

regexSetCursor = r"^(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-?([0-4])?$"
#x-y-duration?       => move
regexMoveOnScreen = r"^(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-(100|[1-9]?[0-9])$"
#x-y-x2-y2        => pick someone and target something
regexCircle= r"^c(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-([1-9])$"
#c x-y-numberOfCircles

def getScreenCoordinates():
    window = pyautogui.getWindowsWithTitle(get_active_app_name())[0]
    xmin = window.left+9
    xmax = window.left-9 + window.width
    ymin = window.top + int((window.height-9 + 80)/2)
    ymax = window.top + window.height-9
    return xmin, xmax, ymin, ymax


def setCursor(x,y,duration):

    xmin, xmax, ymin, ymax = getScreenCoordinates()
    
    newx = xmin + int((xmax-xmin)*x/100)
    newy = ymin + int((ymax-ymin)*y/100)

    coordonates = [newx, newy]

    win32api.SetCursorPos(coordonates)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def moveOnScreen(x1,y1,x2,y2):   

    xmin, xmax, ymin, ymax = getScreenCoordinates()
    x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
    fromX = xmin + int((xmax-xmin)*x1/100)
    fromY = ymin + int((ymax-ymin)*y1/100)
    toX = xmin + int((xmax-xmin)*x2/100)
    toY = ymin + int((ymax-ymin)*y2/100)
    moveFromTo([fromX, fromY],[toX, toY])    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def drawCircle(x,y,numberOfCircle):
    xmin, xmax, ymin, ymax = getScreenCoordinates()
    radius=35
    newx = xmin + int((xmax-xmin)*x/100)
    newy = ymin + int((ymax-ymin)*y/100)
    radius = int((xmax-xmin)*radius/100)

    hexagon_points = hexagon(newx, newy, radius)
    hexagon_points = [(x,y) for x,y in hexagon_points]
    for i, points in enumerate(hexagon_points):
        x, y = points
        if x < xmin:
            x = xmin
        elif x > xmax:
            x = xmax
        if y < ymin:
            y = ymin
        elif y > ymax:
            y = ymax
        hexagon_points[i] = (x, y)

    j=0
    while j<numberOfCircle:
        i=0
        while i<5:
            moveFromTo([hexagon_points[i][0], hexagon_points[i][1]],[hexagon_points[i+1][0], hexagon_points[i+1][1]])
            i+=1
        moveFromTo([hexagon_points[i][0], hexagon_points[i][1]],[hexagon_points[0][0], hexagon_points[0][1]])
    
        #necessary to close the last circle
        j+=1
    i=0
    while i<1:
        moveFromTo([hexagon_points[i][0], hexagon_points[i][1]],[hexagon_points[i+1][0], hexagon_points[i+1][1]])
        i+=1
    

    

def isValidScreenAction(message, regex):
    if(re.match(regex, message, re.IGNORECASE)) : 
        return True
    else:
        return False



def screenAction(message):

    if isValidScreenAction(message, regexSetCursor) == True :
        match =re.match(regexSetCursor, message)
        x = int(match.group(1))
        y = int(match.group(2))
        if (match.group(3)) is None :
            duration = 0.1
        else:
            duration = int(match.group(3))
        setCursor(x,y,duration)

    elif isValidScreenAction(message, regexMoveOnScreen) == True :
        match = re.match(regexMoveOnScreen, message)
        moveOnScreen(match.group(1),match.group(2),match.group(3),match.group(4))

    elif isValidScreenAction(message, regexCircle) == True :
        match =re.match(regexCircle, message)
        x = int(match.group(1))
        y = int(match.group(2))
        numberOfCircle = int(match.group(3))
        drawCircle(x,y,numberOfCircle)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

screenAction('c0-100-3')
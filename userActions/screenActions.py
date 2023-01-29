import pyautogui
import win32api
import win32con
import re
import time
from appDimensions import get_active_app_name
from moveOnScreen import moveFromTo

uselessHeight = 80

regexSetCursor = r"^(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-?([0-4])?$"
regexMoveOnScreen = r"^(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-(100|[1-9]?[0-9])$"
regexCircle= r"^c(100|[1-9]?[0-9])-(100|[1-9]?[0-9])-([1-9])-?([5-9])?$"
# x-y-numberOfCircles-radius?ù

def getScreenCoordinates():
    window = pyautogui.getWindowsWithTitle(get_active_app_name())[0]
    xmin = window.left+9
    xmax = window.left-9 + window.width
    ymin = window.top + int((window.height-9 + 80)/2)
    ymax = window.top + window.height-9
    return xmin, xmax, ymin, ymax


def setCursor():

    match =re.match(regexSetCursor, test)
    x = int(match.group(1))
    y = int(match.group(2))
    if (match.group(3)) is None :
        duration = 0.1
        print("null")
    else:
        duration = int(match.group(3))
    
    xmin, xmax, ymin, ymax = getScreenCoordinates()
    
    newx = xmin + int((xmax-xmin)*x/100)
    newy = ymin + int((ymax-ymin)*y/100)

    coordonates = [newx, newy]

    win32api.SetCursorPos(coordonates)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


test = "c50-50-6"

def drawCircle():
    match =re.match(regexCircle, test)
    x = int(match.group(1))
    y = int(match.group(2))
    xmin, xmax, ymin, ymax = getScreenCoordinates()
    numberOfCircle = int(match.group(3))
    if (match.group(4)) is None :
        radius = int((xmax-xmin)*20/100)
    else:
        radius = int(match.group(4))
    i=0
    
    newx = xmin + int((xmax-xmin)*x/100)
    newy = ymin + int((ymax-ymin)*y/100)

    ##45 45, 55 45, 55 55, 45 55 
    smallerX = newx - radius
    if (smallerX < xmin) :
        smallerX = xmin
    smallerY = newy - radius
    if (smallerY < ymin) :
        smallerY = ymin
    biggerX = newx + radius
    if (biggerX > xmax) :
        biggerX = xmax
    biggerY = newy + radius
    if (biggerY > ymax) :
        biggerY = ymax

    #moveFromTo([xmin, ymin],[xmax, ymax])
    print(xmin, xmax, ymin, ymax)
    print(smallerX, biggerY, smallerX+1, smallerY)
    moveFromTo([smallerX, smallerY],[biggerX-1, smallerY])
    moveFromTo([biggerX, smallerY],[biggerX-1, biggerY])
    moveFromTo([biggerX, biggerY],[smallerX+1, biggerY])
    moveFromTo([smallerX, biggerY],[smallerX+1, smallerY])
    moveFromTo([smallerX, smallerY],[biggerX-1, smallerY])
        
    

if re.match(regexSetCursor, test):
    setCursor()
elif re.match(regexMoveOnScreen, test):
    match =re.match(regexMoveOnScreen, test)

    xmin, xmax, ymin, ymax = getScreenCoordinates()
    
    newfirstx = xmin + int((xmax-xmin)*int(match.group(1))/100)
    newfirsty = ymin + int((ymax-ymin)*int(match.group(2))/100)
    newsecondx = xmin + int((xmax-xmin)*int(match.group(3))/100)
    newsecondy = ymin + int((ymax-ymin)*int(match.group(4))/100)
    moveFromTo([newfirstx, newfirsty],[newsecondx, newsecondy])
elif re.match(regexCircle, test):
    drawCircle()
else:
    print("error")
import win32api
import win32con
import time

def isLess(a,b):
    return a < b
def isGreater(a,b):
    return a > b
# simuler le clic

def moveFromTo(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    # y intercept of our line
    i = p1[1] - m * p1[0]
    # current point
    cP = p1
    # while loop comparison
    comp = isGreater
    # moving left to right or right to left
    inc = -1
    # switch for moving to right
    if (p2[0] > p1[0]):
        comp = isLess
        inc = 1
    # move cursor one pixel at a time
    while comp(cP[0],p2[0]):
        win32api.SetCursorPos(cP)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        #inscrease speed of line
        cP[0] += inc
        # get next point on line
        cP[1] = int(m * cP[0] + i)
        # slow it down
        time.sleep(0.0005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
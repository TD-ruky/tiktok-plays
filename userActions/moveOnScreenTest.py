import win32api
import win32con
import time



def moveFromTo(p1,p2):
    win32api.SetCursorPos(p1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos(p2)


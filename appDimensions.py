import pyautogui
import win32gui
import win32api
import win32con
import time
import pydirectinput
import math
import re

timeToSetup = 1
uselessHeight = 80


def get_active_app_name():
    time.sleep(timeToSetup)
    # Récupère le handle de la fenêtre active
    hwnd = win32gui.GetForegroundWindow()
    # Récupère le nom de l'application active
    app_name = win32gui.GetWindowText(hwnd)
    return app_name

def get_app_dimensions(app_name):
    # Récupère la handle de la fenêtre de l'application
    hwnd = win32gui.FindWindow(None, app_name)
    #Récupère les dimensions de la fenêtre en pixels
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    return width, height, left, top, right, bottom
 





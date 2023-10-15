import win32gui, win32api
import keyboard, wx, time
import pyscreenshot
from pix2tex.cli import LatexOCR


app = wx.App()
s = wx.ScreenDC()
s.Pen = wx.Pen("#FF9999", width=4)
s.Brush = wx.Brush("white", wx.TRANSPARENT)

model = LatexOCR()

def draw_a_cross(x,y):
    s.DrawLine(x-10,y,x+10,y)
    s.DrawLine(x,y-10,x,y+10)
    
def evaluate(x1,y1,x2,y2):
    image = pyscreenshot.grab(bbox=(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    print('Recognizing...')
    print(model(image))

def draw_screenarea():
    m = win32gui.GetCursorPos()
    time.sleep(.1)
    pim = win32api.GetKeyState(0x01)
    pam = pim
    n =[0,0]
    while pim == pam:
        n = win32gui.GetCursorPos()
        pam = win32api.GetKeyState(0x01)
        draw_a_cross(m[0],m[1])
    draw_a_cross(m[0],m[1])
    draw_a_cross(n[0],n[1])
    s.Clear()
    evaluate(m[0],m[1],n[0],n[1])

def take_screenshot():
    pim = win32api.GetKeyState(0x01)
    pam = pim
    while pim == pam:
        pam = win32api.GetKeyState(0x01)
    draw_screenarea()
        
keyboard.add_hotkey("ctrl+alt+q", take_screenshot)
try:
    while True:
        ...
except KeyboardInterrupt:
    pass
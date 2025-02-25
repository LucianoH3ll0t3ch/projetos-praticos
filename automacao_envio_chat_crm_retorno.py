import pyautogui as ptg
import random

x = 0
def iniciar():
    
    while(x < 50):
        x=+1
        ptg.PAUSE=1
        ptg.click(74,705)
        ptg.click(242,688)
        ptg.click(256,623)
        ptg.moveTo(74,705)
        ptg.scroll(-56)
iniciar()
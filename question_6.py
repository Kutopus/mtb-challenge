from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui as pg
from PIL import Image
import os
import time

s = Service(r'C:\Programação\Python\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.set_window_size(1920, 1080)

url = 'https://metrobi.com/'

browser.get(url)
browser.save_screenshot('metrobi.png')

browser.close()

img = Image.open("metrobi.png")
img.show()

x, y, z, w = pg.locateOnScreen('metrobi_fundo.png', grayscale=True, confidence=.5)

os.system('taskkill /f /im Microsoft.Photos.exe')

print("________________________")
print("Local:")
print(f"Top: {y}, Left: {x}")

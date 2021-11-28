from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui as pg
import cv2
import time

# Your Chromedriver path
s = Service(r'C:\Programação\Python\chromedriver.exe')

browser = webdriver.Chrome(service=s)
# You can change the windows size
size_x, size_y = 1920, 1080
browser.set_window_size(size_x, size_y)

# You can change the URL too
# (https://metrobi.com / https://deliver.metrobi.com/signin)
url = 'https://metrobi.com'

browser.get(url)
browser.save_screenshot('metrobi.png')

browser.close()

img = cv2.imread('metrobi.png')
cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Image", img)

try:
    x, y, z, w = pg.locateOnScreen('metrobi_fundo.png', grayscale=True, confidence=.5)
except TypeError:
    x, y, z, w = pg.locateOnScreen('metrobi_fundo_2.png', grayscale=True, confidence=.5)

print(f"Coordinates:\nLeft (X): {x} | Top (Y): {y}")

pg.moveTo(x, y)

print('----------------------------')

cv2.destroyAllWindows()

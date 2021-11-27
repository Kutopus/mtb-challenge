from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui as pg

s = Service(r'C:\Programação\Python\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.set_window_size(1920, 1080)

url = 'https://metrobi.com/'

browser.get(url)
browser.save_screenshot('metrobi.png')

x, y, z, w = pg.locateOnScreen('metrobi_fundo.png', grayscale=True, confidence=.9)

print(f"Coordinates:\nLeft (X): {x} | Top (Y): {y}")

# To test
# pg.click(x, y)

browser.close()

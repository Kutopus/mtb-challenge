from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui as pg
import cv2

# Your Chromedriver path
s = Service(r'C:\Programação\Python\chromedriver.exe')
browser = webdriver.Chrome(service=s)

# You can change the windows size
# (1920, 1080 / 640, 1136)
size_x, size_y = 0, 0
browser.set_window_size(size_x, size_y)

# You can change the URL too
# (https://metrobi.com / https://deliver.metrobi.com/signin)
url = ''

browser.get(url)
browser.save_screenshot('metrobi.png')

browser.close()

img = cv2.imread('metrobi.png', cv2.COLOR_GRAY2BGR)
cv2.setWindowProperty("Image", cv2.WINDOW_AUTOSIZE, cv2.WINDOW_KEEPRATIO)
cv2.imshow("Image", img)
cv2.waitKey(500)

try:
    x, y, z, w = pg.locateOnScreen('metrobi_fundo.png', grayscale=True, confidence=.9)
except TypeError:
    x, y, z, w = pg.locateOnScreen('metrobi_fundo_2.png', grayscale=True, confidence=.6)
except Exception:
    print("I can't find that, try to change the confidence :)")

# To test
pg.moveTo(x, y)

print(f"Coordinates:\nLeft (X): {x} | Top (Y): {y}")
print('----------------------------')

cv2.destroyAllWindows()

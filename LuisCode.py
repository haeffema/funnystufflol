# Test um stats automatisch auslesen zu lassen

from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Users\noetz\Documents\Python Projekte\chromedriver')
driver.get('https://www.pokewiki.com')
time.sleep(5)
driver.quit()

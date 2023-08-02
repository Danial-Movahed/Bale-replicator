import sys
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://google.com")
print("gooogle!")
driver.save_screenshot('sample_screenshot_1.png')
driver.close()

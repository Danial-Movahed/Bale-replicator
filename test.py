import sys
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--proxy-server=socks5://127.0.0.1:40000')
driver = webdriver.Chrome(options=options)
driver.get("https://ping.eu")
print("piiing!")
driver.save_screenshot('sample_screenshot_1.png')
driver.close()

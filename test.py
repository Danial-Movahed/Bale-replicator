import sys
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

proxyhost = "127.0.0.1"
proxyport = 40000
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', proxyhost)
options.set_preference('network.proxy.socks_port', proxyport)
driver = webdriver.Firefox(options=options)
driver.get("https://ping.eu")
print("piiing!")
driver.save_screenshot('sample_screenshot_1.png')
driver.close()

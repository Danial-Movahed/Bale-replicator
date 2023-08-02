import sys
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

proxyhost = "127.0.0.1"
proxyport = 40000

class WebDriver:
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        
        if len(sys.argv) > 1:
            self.options.add_argument('--headless')
            self.options.set_preference('network.proxy.type', 1)
            self.options.set_preference('network.proxy.socks', proxyhost)
            self.options.set_preference('network.proxy.socks_port', proxyport)

        self.driver = webdriver.Firefox(options=self.options)
        self.GetUrl("https://web.bale.ai/chat")
        self.Login()
        sleep(20)
        self.SkipTutorial()
        sleep(1)
        self.weeb = self.FindWeeb()
        self.SendMessage(self.weeb, "Dalam weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeb!")

    def FindWeeb(self):
        return self.driver.find_element(By.XPATH,"//div[@class='TopBlock_Name__rQZPl' and contains(., 'امیرحسام سجودی')][1]")

    def SendMessage(self, person, message):
        self.driver.execute_script("arguments[0].click();", person)
        sleep(5)
        textBox = self.driver.find_element(By.ID, "main-message-input")
        textBox.send_keys(message)
        sleep(1)
        textBox.send_keys(Keys.ENTER)

    def GetUrl(self, url):
        self.driver.get(url)

    def SetPhoneNumber(self, phoneNumber):
        telNumberElement = self.driver.find_element(By.ID, "شماره همراه")
        sleep(5)
        telNumberElement.send_keys(phoneNumber)
        sleep(0.4)
        telNumberElement.send_keys(Keys.ENTER)

    def SetOTP(self, otp):
        otpElement = self.driver.find_element(By.ID, "کد ورود")
        sleep(1)
        otpElement.send_keys(otp)
        sleep(0.4)
        try:
            otpElement.send_keys(Keys.ENTER)
        except:
            pass

    def SkipTutorial(self):
        self.driver.find_element(By.TAG_NAME, "body").click()

    def Login(self):
        self.SetPhoneNumber("9012324766")
        self.SetOTP(input("Please enter your otp: "))
        # self.driver.close()

wd = WebDriver()

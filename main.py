import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class WebDriver:
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        if len(sys.argv) > 1:
            self.options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=self.options)
    def run(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        elem = self.driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        self.driver.close()

wd = WebDriver()
wd.run()
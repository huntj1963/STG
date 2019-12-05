# Generated by Selenium IDE
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Challenge2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def teardown(self,):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com/")
        self.driver.find_element(By.ID, "input-search").click()
        self.driver.find_element(By.ID, "input-search").send_keys("exotics")
        self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)
        time.sleep(5)
# I could not figure out how to search for the specific text "PORSCHE" then do an assert hard stop.
# Instead I used Selenium to assert the text.
        self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").text == "PORSCHE"


if __name__ == '__main__':
    unittest.main()
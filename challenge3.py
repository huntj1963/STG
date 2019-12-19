import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_challenge3forloop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        for count in elements:
            print (count.text + ": " + count.get_attribute("href"))


    def test_challenge3whileloop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[3]//a")
        i = 0
        while i < len(elements):
            print(elements[i].text + ": " + elements[i].get_attribute("href"))
            i += 1

if __name__ == '__main__':
    unittest.main()

import unittest
import HtmlTestRunner
from selenium import webdriver
import os,time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../chromedriver_2.45")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_something(self):
        self.driver.get("https://www.google.com")
        self.assertEqual(self.driver.title, "Google", "Title assertion failed")


    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/ramnath/PycharmProjects/Selenium_Python/reports'))

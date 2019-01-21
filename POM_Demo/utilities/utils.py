from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from POM_Demo.utilities.MyListener import MyListener
import os

class utils:

    def launch_browser(self, browser_name):

        browser_name = browser_name.lower()

        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path="/Users/ramnath/PythonFramework/chromedriver_2.45")
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path="/Users/ramnath/PythonFramework/geckodriver_mac")

        # ef_driver = EventFiringWebDriver(driver, MyListener())
        driver.implicitly_wait(30)
        driver.maximize_window()



        return driver


    def quit_browser(self, driver):
        driver.quit()

from selenium import webdriver

import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

d2 = webdriver.Firefox(executable_path=os.getcwd() + os.path.sep + "geckodriver_mac")
d2.maximize_window()
d2.get("https://www.google.com")
wait = WebDriverWait(d2, 30)

wait.until(ec.element_to_be_clickable((By.NAME, "q")))
element = d2.find_element_by_name("q")
element.send_keys("ramnath gokul")
element.send_keys(Keys.ENTER)
time.sleep(5)
d2.quit()
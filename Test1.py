import os
import time

from selenium import webdriver
from selenium.webdriver import Proxy, FirefoxProfile
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as firefox_options

p = Proxy()
p.http_proxy = "1.1.1.1"

fp = FirefoxProfile()
fp.accept_untrusted_certs = True
fp.assume_untrusted_cert_issuer = False
# fp.set_proxy(proxy)

chrome_options = Options()
firefox_options = firefox_options()
firefox_options.headless = True
chrome_options.headless = False

# driver = webdriver.firefox(executable_path=os.getcwd() + os.path.sep + "geckodriver_mac")
driver = webdriver.Chrome(options=chrome_options, executable_path=os.getcwd() + os.path.sep + "chromedriver_2.45")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("ramnath gokul", Keys.SHIFT)
driver.find_element_by_name("q").send_keys(Keys.ENTER)
# driver.find_element_by_name("btnK").click()
time.sleep(2)
driver.quit()
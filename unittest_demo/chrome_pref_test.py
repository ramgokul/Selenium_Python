from selenium.webdriver.chrome.options import Options
from selenium import webdriver


map = dict()
map['profile.default_content_settings.popups'] = False
x = Options()
x.add_experimental_option("prefs", map)
x.headless = True

driver = webdriver.Chrome(executable_path="/Users/ramnath/PythonFramework/chromedriver_2.45", chrome_options=x)
driver.maximize_window()
driver.quit()
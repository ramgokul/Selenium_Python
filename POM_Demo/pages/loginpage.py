from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from POM_Demo.locators.locators import locators
from selenium.webdriver.support import expected_conditions as EC

class loginpage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def login_to_crm(self, url, username, password):
        try:
            self.driver.get(url)

            self.wait.until(EC.element_to_be_clickable((By.ID, locators.username_input_id)))
            self.driver.find_element_by_id(locators.username_input_id).send_keys(username)
            # time.sleep(5)

            self.wait.until(EC.element_to_be_clickable((By.ID, locators.password_input_id)))
            # self.driver.find_element_by_id(locators.password_input_id).click()
            self.driver.find_element_by_id(locators.password_input_id).send_keys(password)

            self.driver.find_element_by_id(locators.login_button_id).click()
        except Exception as error:
            print("login to crm failed : ", error)
            raise


    def logout_of_crm(self):
        try:
            self.driver.find_element_by_id(locators.welcome_link_id).click()
            self.driver.find_element_by_xpath(locators.logout_link_xpath).click()
            self.wait.until(EC.element_to_be_clickable((By.ID, locators.username_input_id)))
        except Exception as error:
            print("logout of crm failed : ", error)
            raise

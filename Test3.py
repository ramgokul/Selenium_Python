from selenium import webdriver
import os, time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class some_class:

    def select_box_behavior(self):

        driver = webdriver.Chrome(executable_path= os.getcwd() + os.path.sep + "chromedriver_2.45")
        driver.maximize_window()
        driver.implicitly_wait(10)
        #
        # driver.get("https://www.facebook.com/")
        # driver.back()
        # driver.forward()
        # driver.find_element_by_css_selector("#email").send_keys("ramnath1109@gmail.com")
        # # time.sleep(2)
        # driver.find_element_by_css_selector("#email").clear()
        #
        # Select(driver.find_element_by_id("day")).select_by_visible_text("10")
        # Select(driver.find_element_by_id("month")).select_by_visible_text("Nov")
        # Select(driver.find_element_by_id("year")).select_by_visible_text("1982")
        # driver.find_element_by_xpath("//*[@id='u_0_9']/following::input").click()
        # print("Is selected? = ", driver.find_element_by_xpath("//*[@id='u_0_9']/following::input").is_selected())

        # Action chains

        driver.get("https://jqueryui.com/menu/")
        action = ActionChains(driver)
        driver.switch_to.frame(0)
        action.move_to_element(driver.find_element_by_xpath("//*[@id='ui-id-9']")).perform()
        time.sleep(5)
        driver.switch_to.default_content()
        driver.quit()



        # select_box_behavior()


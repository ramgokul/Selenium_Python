from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener



class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

    def on_exception(exception, driver):
        print("inside on_exception")
        driver.save_screenshot("abc.png")


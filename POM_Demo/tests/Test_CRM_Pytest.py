
from selenium import webdriver
import pytest, logging

class Test_CRM_Pytest:

    @pytest.fixture()
    def test_setup(self, test_get_env_variables):

        global driver

        if test_get_env_variables['browser'] == 'chrome':
            driver = webdriver.Chrome(executable_path="/Users/ramnath/PythonFramework/chromedriver_2.45")

        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.quit()

    # @pytest.fixture(autouse=True, scope='session')
    # def test_get_env_variables(self, request):
    #     global url_value
    #     url_value = request.config.getoption('url')
    #     print(url_value)

    @pytest.mark.orange
    def test_crm_login(self, test_setup, test_get_env_variables):
        driver.get(test_get_env_variables['url'])
        assert driver.title == "OrangeHRM"

    @pytest.mark.skip(reason="Test broken due to defect AM-4526")
    def test_google_page(self, test_setup, test_get_env_variables):
        driver.get(test_get_env_variables['url'])
        assert driver.title == "Googlee"

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_gmail_page(self, test_setup, test_get_env_variables):
        # print(test_get_env_variables['url_value'])

        logging.basicConfig(format="%{asctime}s")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        driver.get(test_get_env_variables['url'])
        logger.info("Test completed")
        assert driver.title == "Gmail"


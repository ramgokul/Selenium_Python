import unittest
import sys
from POM_Demo.utilities.utils import utils
from POM_Demo.pages.loginpage import loginpage


class CRMTestCase(unittest.TestCase):
    # username = "Admin"
    # password = "admin123"
    url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"

    def setUp(self):
        self.utils = utils()
        self.driver = self.utils.launch_browser("chrome")
        self.loginpage = loginpage(self.driver)

    def test_login_functionality(self):
        self.loginpage.login_to_crm(self.url, map['username'], map['password'])
        self.loginpage.logout_of_crm()


    def tearDown(self):
        self.utils.quit_browser(self.driver)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        # CRMTestCase.username = sys.argv[1]
        # CRMTestCase.password = sys.argv[2]
        map = dict()

        # Passing arguments like a dictionary (For eg, username:Admin)
        for x in range(1, len(sys.argv)):
            print(sys.argv[x])
            arg_value = sys.argv[x].strip().split(":")
            print(arg_value[0])
            map[arg_value[0]] = arg_value[1]
        del sys.argv[1:]
    unittest.main(unittest.main())

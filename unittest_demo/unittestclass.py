import unittest
import HtmlTestRunner
from unittest_demo.Examples import Example


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before class\n")

    def setUp(self):
        print("before method")

    def test_addition_functionality(self):
        result = Example().add_numbers(5, 10)
        self.assertEqual(result, 15)
        print("Addition test passed")

    def test_subtraction_functionality(self):
        result = Example().sub_numbers(20, 10)
        self.assertEqual(result, 10)
        print("Subtraction test passed")

    def tearDown(self):
        print("After Method")

    @classmethod
    def tearDownClass(cls):
        print("After class")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/ramnath/PycharmProjects/Selenium_Python/reports'))

"""
This module simulates user behavior via selenium and the default browser.
Test of logout functionality.
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFavorite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_logout(self):
        # Test name: logout
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(2576, 1066)
        self.driver.find_element(By.CSS_SELECTOR, "#loginbtn img").click()
        self.driver.find_element(By.ID, "id_login").click()
        self.driver.find_element(By.ID, "id_login").click()
        self.driver.find_element(By.ID, "id_login").send_keys(
            "testpurbeurre@gmail.com")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("AZERTY1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "#logoutbtn img").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

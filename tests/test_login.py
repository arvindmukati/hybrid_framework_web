import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from utilities import data_source

from base.webdriver_listener import WebDriverWrapper


class TestAddEmployee(WebDriverWrapper):
    @pytest.mark.parametrize('username, password, expected_page', [
        ("standard_user", "secret_sauce", "Products")])
    def test_valid_login(self, username, password, expected_page):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        actual_page = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        assert_that(actual_page).is_equal_to(expected_page)

    @pytest.mark.parametrize('username, password, expected_error', data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        actual_error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert_that(actual_error).is_equal_to(expected_error)

    @pytest.mark.parametrize('username, password, expected_page', data_source.test_valid_login_data)
    def test_valid_login_using_csv_and_javascript(self, username, password, expected_page):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.execute_script("document.querySelector('#login-button').click()")
        actual_page = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        assert_that(actual_page).is_equal_to(expected_page)

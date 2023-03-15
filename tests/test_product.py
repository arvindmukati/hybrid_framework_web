from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.webdriver_listener import WebDriverWrapper


class TestAddEmployee(WebDriverWrapper):

    def test_place_order(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        select_view = Select(self.driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']"))
        select_view.select_by_value("hilo")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        self.driver.find_element(By.ID,"checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys('Test')
        self.driver.find_element(By.ID, "last-name").send_keys('User')
        self.driver.find_element(By.ID,'postal-code').send_keys('00000')
        self.driver.find_element(By.ID, 'continue').click()
        price = self.driver.find_element(By.XPATH,"//div[@class='inventory_item_price']").text
        assert_that(price).is_equal_to("$49.99")
        self.driver.find_element(By.XPATH, "//button[@id='finish']").click()
        checkout_page = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        assert_that(checkout_page).is_equal_to("Checkout: Complete!")

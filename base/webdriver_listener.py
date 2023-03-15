from selenium import webdriver
import pytest


class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/")
        yield
        self.driver.quit()


class WebDriverWrapper1:
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://testpages.herokuapp.com/styled/csspseudo/css-hover.html")
        yield
        self.driver.quit()

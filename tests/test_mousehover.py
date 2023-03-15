from assertpy import assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper1


class TestMouseHover(WebDriverWrapper1):
    def test_mouse_hover(self):
        ele = self.driver.find_element(By.ID, "hoverpara")
        a = ActionChains(self.driver)
        a.move_to_element(ele).perform()
        text_hover = self.driver.find_element(By.ID, "hoverparaeffect").text
        assert_that(text_hover).is_equal_to("You can see this paragraph now that you hovered on the above 'button'.")

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.customer_input import CustomerInput

# 首页功能
class Main(BasePage):
    def customer_input(self):
        self._driver.find_element(By.LINK_TEXT, '机会录入').click()
        self._driver.find_element(By.ID, 'inputBtn').click()
        return CustomerInput(self._driver)

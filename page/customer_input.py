from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class CustomerInput(BasePage):
    def add_customer(self, customername=None, contactPhone=None):

        """
        成员录入页面填写成员信息
        姓名、手机号、关联子、渠道、所属部门
        """
        self._driver.switch_to.frame(1)
        customer = (By.CSS_SELECTOR, 'input[name="customerName"]')
        self.wait(5, expected_conditions.visibility_of_element_located(customer))
        self.find(*customer).send_keys(customername)
        self.find(By.NAME, 'contactPhone').send_keys(contactPhone)
        self.find(By.CSS_SELECTOR, '#fc_3708 .filter-option').click()
        self.find(By.CSS_SELECTOR, '#fc_3708 li[rel="1"]').click()
        self.find(By.CSS_SELECTOR, '#channel .filter-option').click()
        self.find(By.LINK_TEXT, "搜狗").click()
        self.find(By.CSS_SELECTOR, '#group .filter-option').click()
        self.find(By.LINK_TEXT, "公司").click()
        # todo:其他注册项
        self.find(By.ID, 'submit').click()
        self.find(By.CSS_SELECTOR, ".btn-primary:nth-child(1)").click()
        self.find(By.ID, "input_colse").click()


    def wait(self, timeout, method):
        """定义显示等待"""
        WebDriverWait(self._driver, timeout).until(method)
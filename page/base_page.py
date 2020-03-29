import json
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    _driver = None
    def __init__(self, driver:WebDriver=None):
        """登陆后抓取cookie信息，便于之后自动登录"""
        if driver == None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
            self._driver.get('http://uctcrm.yunduoketang.cn/customer/show/publicData')
            self._driver.add_cookie({'name': 'SSID', 'value': 'cf2765c2fce34a03b8279b08c4eb62d6'})
            self._driver.get('http://uctcrm.yunduoketang.cn/customer/show/publicData')
        else:
            self._driver = driver

    def find(self, by, locator=""):
        """封装 find_element 方法"""
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def close(self):
        """10s后自动关闭浏览器"""
        time.sleep(10)
        self._driver.quit()
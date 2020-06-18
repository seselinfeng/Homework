# Generated by Selenium IDE
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLogin():
    """
      该模块用于企业微信免登录测试
      """
    def setup_method(self, method):
        self.driver = webdriver.Chrome('/Users/apple/Documents/web/chromedriver')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open("cookies")
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(5)
        db.close()

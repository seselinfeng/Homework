from selenium.webdriver.common.by import By

from EnterpriseWeChat.page.contacts import Contacts
from EnterpriseWeChat.page.base_page import BasePage


class Main(BasePage):
    """主页面"""
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contacts(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts > span").click()
        return Contacts(self._driver)

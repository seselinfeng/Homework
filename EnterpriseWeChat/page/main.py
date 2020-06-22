from selenium.webdriver.common.by import By

from EnterpriseWeChat.page.add_member import AddMember
from EnterpriseWeChat.page.base_page import BasePage


class Main(BasePage):
    """主页面"""
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts > span").click()

        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, "#member_list"))
            if elements_len > 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elements_len > 0

        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        self.wait_for_element(wait_add_member)
        return AddMember(self._driver)

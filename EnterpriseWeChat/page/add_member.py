from selenium.webdriver.common.by import By

from EnterpriseWeChat.page.base_page import BasePage


class AddMember(BasePage):
    """添加成员页面"""
    def add_member(self, username, acctid, phone):
        """
        添加成员操作
        :return:
        """
        from EnterpriseWeChat.page.contacts import Contacts
        self._params["username"] = username
        self._params["acctid"] = acctid
        self._params["phone"] = phone

        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, "#username"))
            return elements_len > 0
        self.wait_for_element(wait_add_member)
        self.steps('../data/addmember.yaml')
        return Contacts(self._driver)

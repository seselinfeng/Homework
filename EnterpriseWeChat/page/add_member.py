from selenium.webdriver.common.by import By

from EnterpriseWeChat.page.base_page import BasePage


class AddMember(BasePage):
    """添加成员页面"""

    def add_member(self, username, acctid, phone):
        """
        添加成员操作
        :return:
        """
        self._params["username"] = username
        self._params["acctid"] = acctid
        self._params["phone"] = phone

        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, "#username"))
            return elements_len > 0

        self.wait_for_element(wait_add_member)
        # self.find(By.CSS_SELECTOR, "#username").send_keys("12345678")
        # self.find(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("12345678")
        # self.find(By.CSS_SELECTOR, "#memberAdd_phone").send_keys("15000000001")
        # self.find(By.CSS_SELECTOR, ".member_edit>form>div:nth-last-child(1)>a:nth-child(2)").click()
        self.steps('../data/addmember.yaml')

    def update_page(self):
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        # 对 1/10 进行切割
        return [int(x) for x in content.split('/', 1)]

    def get_member(self, username):
        """
        获取新增成员并断言
        :return:
        """
        self.wait_for_click((By.CSS_SELECTOR, ".ww_checkbox"))
        username_elements_length = len(self.finds(By.CSS_SELECTOR,"#member_list > tr "))
        if username_elements_length == 20:
            # 翻页操作
            cur_page, total_page = self.update_page()
            while True:
                elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
                for element in elements:
                    if username == element.get_attribute("title"):
                        return True
                cur_page = self.update_page()[0]
                if cur_page == total_page:
                    return False
                self.find(By.CSS_SELECTOR, '.js_next_page').click()
        else:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if username == element.get_attribute("title"):
                    return True
            else:
                return False

import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from EnterpriseWeChat.common.log import Log
from EnterpriseWeChat.page.add_member import AddMember
from EnterpriseWeChat.page.base_page import BasePage


class Contacts(BasePage):
    """通讯录页面"""
    _log = Log()

    def _update_page(self):
        """
        切割分页符
        :return:
        """
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        self._log.info("页码为{}".format(content))
        # 对 1/10 进行切割
        return [int(x) for x in content.split('/', 1)]

    def _get_member_count(self):
        """
        获取通讯录当前人数
        :return:
        """
        username_numbers = int(
            re.findall(r"\((.+?)人\)", self.find(By.CSS_SELECTOR, ".js_member_count").get_attribute("innerHTML"))[0])
        self._log.info("当前已邀请用户数:{}".format(username_numbers))
        return username_numbers

    def goto_add_member(self):
        """
        跳转到添加用户界面
        :return:
        """
        self.wait_for_click((By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)'))
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember()

    def get_member(self, username):
        """
        获取通讯录成员并断言
        :return: True 用户已存在  False 用户未存在
        """
        self.wait_for_click((By.CSS_SELECTOR, ".ww_checkbox"))
        username_numbers = self._get_member_count()
        if username_numbers > 20:
            # 翻页操作
            cur_page, total_page = self._update_page()
            while cur_page != 1:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowLeftNormal").click()
                cur_page -= 1
            while True:
                elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
                for element in elements:
                    if username == element.get_attribute("title"):
                        return True
                cur_page = self._update_page()[0]
                if cur_page == total_page:
                    return False
                else:
                    self.find(By.CSS_SELECTOR, '.js_next_page').click()
        else:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if username == element.get_attribute("title"):
                    return True
            else:
                return False

    def _do_del_member(self, element: WebElement):
        """
        删除用户操作
        :param element:
        :return:
        """
        element.click()
        self.wait_for_click((By.CSS_SELECTOR, ".js_del_member"))
        self.find(By.CSS_SELECTOR, ".js_del_member").click()
        self.wait_for_click((By.CSS_SELECTOR, ".ww_dialog_foot>a:nth-child(1)"))
        self.find(By.CSS_SELECTOR, ".ww_dialog_foot>a:nth-child(1)").click()
        return True

    def del_member(self, username):
        self.wait_for_click((By.CSS_SELECTOR, ".ww_checkbox"))
        username_numbers = self._get_member_count()
        if username_numbers > 20:
            # 翻页操作
            cur_page, total_page = self._update_page()
            while True:
                elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
                for element in elements:
                    if username == element.get_attribute("title"):
                        return self._do_del_member(element)
                cur_page = self._update_page()[0]
                if cur_page == total_page:
                    return False
                self.find(By.CSS_SELECTOR, '.js_next_page').click()
        else:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if username == element.get_attribute("title"):
                    return self._do_del_member(element)
            else:
                return False

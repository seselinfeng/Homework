from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from CorporateWeChat.page.BasePage import BasePage


class MemberInvite(BasePage):
    """添加成员页面"""

    def addmember_by_manul(self):
        """
        手动输入添加
        :return: 跳转到添加成员详情页
        """
        from CorporateWeChat.page.ContactAdd import ContactAdd
        self.find(MobileBy.ID, 'com.tencent.wework:id/h3a').click()
        return ContactAdd(self._driver)

    def get_toast(self):
        # return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast]").text
        # 用于生成xpath定位 相当于 "//*[@text='没有找到用户名或密码']"
        toast_message = "添加成功"
        message = '//*[@text=\'{}\']'.format(toast_message)
        # 获取toast提示框内容
        result = WebDriverWait(self, 5).until(lambda x: x.find(MobileBy.XPATH, message)).text
        return result

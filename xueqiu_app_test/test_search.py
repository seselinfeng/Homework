import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
import time


class TestSearch:
    def setup_class(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "S2D0219430000212",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true",  # 记住关闭首次启动弹窗状态，再次启动不会打开弹窗
            'unicodeKeyBoard': True,  # 支持中文键盘输入
            'skipDeviceInitialization' : True,
            'skipLogcatCapture' : True,
            'skipServerInstallation' : True,
            'resetKeyBoard': True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def teardown(self):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize("search_key,search_value",[('alibaba', 'BABA'), ('xiaomi', '01810')])
    def test_search(self, search_key, search_value):
        # 点击主页搜索框
        WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search")).click()
        # 输入查询条件
        WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")).send_keys(search_key)
        # 找到要查询的股票后点击
        WebDriverWait(self.driver,5).until(lambda x:x.find_element(MobileBy.XPATH, f"//*[@text='{search_value}']")).click()
        # 点击添加自选按钮
        WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element(MobileBy.XPATH, f"//*[@text='{search_value}']/../../..//*[@text='加自选']")).click()
        self.driver.implicitly_wait(5)
        # 用于生成xpath定位 相当于 "//*[@text='没有找到用户名或密码']"
        toast_message = "已关注"
        message = '//*[@text=\'{}\']'.format(toast_message)
        # 获取toast提示框内容
        result = WebDriverWait(self, 5).until(lambda x: x.find(MobileBy.XPATH,message)).text
        # result = WebDriverWait(self.driver, 5).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/followed_btn']")).text
        assert result == "已关注"

import logging
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _error_num = 0
    _max_num = 0
    _black_list = [(MobileBy.XPATH, "//*[@text='确认']"), (MobileBy.XPATH, "//*[@text='下次再说']"),
                   (MobileBy.XPATH, "//*[@text='确定']")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
        # 所有弹窗默认允许
        self._driver.switch_to.alert.accept()

    def find(self, locator, value: str = None):
        element: WebElement
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                ele_list = self._driver.find_element(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)
            raise e

    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        try:
            element_text = self._driver.find_element(*locator).text if isinstance(locator,
                                                                                  tuple) else self._driver.find_element(
                locator, value).text
            # 找到之前 _error_num 归0
            self._error_num = 0
            # 隐式等待回复原来的等待，
            self._driver.implicitly_wait(10)
            return element_text
        except Exception as e:
            # 出现异常， 将隐式等待设置小一点，快速的处理弹框
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            # 处理黑名单里面的弹框
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return self.find_and_get_text(locator, value)
            raise e

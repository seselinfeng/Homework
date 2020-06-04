import inspect
import json
import yaml
from appium.webdriver import webdriver, WebElement

from FrameworkOptimization.common.log import Log
from FrameworkOptimization.pages.decorator import handle_black


class BasePage:
    _params = {}  # 参数化的数据

    def __init__(self, driver: webdriver = None):
        self._driver = driver
        self._log = Log()

    def set_implicitly_wait(self, time):
        """
        设置隐式等待时间
        :param time:
        :return:
        """
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        """
        保存截图
        :param name:
        :return:
        """
        self._driver.save_screenshot(name)

    @handle_black
    def find(self, locator, value: str = None):
        """
        查找元素
        :param locator:
        :param value:
        :return:
        """
        element: WebElement = None
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def finds(self, locator, value: str = None):
        """
        查找多个元素
        :param locator:
        :param value:
        :return:
        """
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def steps(self, path: str = None):
        """
        封装操作步骤以及操作数据的数据驱动
        :param path:
        :return:
        """
        element: WebElement or str = None
        with open(path, encoding='utf-8') as f:
            # 获取调用函数名称
            name = inspect.stack()[1].function
            # 反射原理获取当前函数的yaml数据驱动
            steps = yaml.safe_load(f)[name]
            # 序列化steps 为字符串 Serialize ``obj`` to a JSON formatted ``str``.
            raw = json.dumps(steps)
            # 将yaml文件中特殊格式字符串转义为数据  ${name} --> alibaba
            for key, value in self._params.items():
                raw = raw.replace('${' + key + '}', value)
            # 反序列化
            steps = json.loads(raw)
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step.get('by'), step.get('locator'))
                if 'action' in step.keys():
                    action = step.get('action')
                    if action == 'click':
                        # 点击事件
                        element.click()
                    if action == 'send_keys':
                        # 输入文本
                        element.send_keys(step.get('value'))
                    if action == 'get_text':
                        # 获取文本
                        element = element.text
                    if action == 'swipe':
                        # 滑动事件,从一个坐标滑动到另一个坐标
                        self._driver.swipe(step.get('start_x'), step.get('start_y'), step.get('end_x'),
                                           step.get('end_y'), duration=step.get('duration'))
                    if action == 'scroll':
                        # 滑动事件，从一个元素滑动到另一个元素
                        self._driver.scroll(step.get('origin_el'), step.get('destination_el'))
        return element

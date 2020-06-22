import inspect
import json

import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from EnterpriseWeChat.common.log import Log


class BasePage():
    """基类"""
    _driver = None
    _base_url = ""
    _params = {}  # 参数化的数据
    log = Log()

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome("/Users/apple/Documents/web/chromedriver", options=options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver
        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self, by, locator):
        """
        查找元素
        :param by:
        :param locator:
        :return:
        """
        try:
            return self._driver.find_element(by, locator)
        except NoSuchElementException as e:
            self.log.error(e)

    def finds(self, by, locator):
        """
        查找多个元素
        :param by:
        :param locator:
        :return:
        """
        try:
            return self._driver.find_elements(by, locator)
        except NoSuchElementException as e:
            self.log.error(e)

    def wait_for_click(self, locator, timeout=10):
        """
        显示等待，直到某个元素可点击
        :param locator:
        :param timeout:
        :return:
        """
        WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_element(self, condtions, timeout=10):
        """
        显示等待，直到condtions方法返回值为true
        :param condtions:
        :param timeout:
        :return:
        """
        WebDriverWait(self._driver, timeout).until(condtions)

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
            self.log.info("steps:{}".format(steps))
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
        return element

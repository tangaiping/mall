from selenium import webdriver
import time
from base.find_element import FindElement
from log.log import Log

logger = Log()
log = logger.get_log()


class ActionMethod(object):

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        log.info('打开浏览器成功！')

    # 输入url
    def get_url(self, url):
        self.driver.get(url)
        log.info('请求url成功！')

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 点击
    def click_element(self, key):
        self.get_element(key).click()
        time.sleep(2)

    # 输入
    def send_keys(self, value, key):
        element = self.get_element(key)
        element.send_keys(str(value))

    # 等待
    def sleep_time(self):
        time.sleep(20)

    # 获取title
    def get_title(self):
        return self.driver.title
        log.info('成功获取title！')

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()
        log.info('关闭浏览器成功！')
        logger.close_hadle()

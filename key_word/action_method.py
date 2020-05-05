from selenium import webdriver
import time
from base.find_element import FindElement


class ActionMethod(object):

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入url
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 点击
    def click_element(self, key):
        self.get_element(key).click()

    # 输入
    def send_keys(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 等待
    def sleep_time(self):
        time.sleep()

    # 获取title
    def get_title(self):
        return self.driver.title

    # 关闭浏览器
    def colse_browser(self):
        self.driver.close()

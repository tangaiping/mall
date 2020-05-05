from utils.read import Read
from selenium import webdriver


class FindElement(object):
    def __init__(self, driver):
       self.driver = driver

    def get_element(self, key):
        read = Read()
        data = read.get_value(key)
        by = data.split(':')[0]
        value = data.split(':')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            if by == 'name':
                return self.driver.find_element_by_name(value)
            if by == 'class':
                return self.driver.find_element_by_class_name(value)
            if by == 'css':
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None


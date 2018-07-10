#!/usr/bin/env python3
# coding:utf-8

from selenium.webdriver.common.by import By
from PageObject import basepage
from Common import mydriver
import time


class BaiduPage(basepage.BasePage):
    """百度首页，定义页面通用属性和方法"""

    url = 'https://www.baidu.com'
    keyword_loc = (By.ID, 'kw')
    search_loc = (By.ID, 'su')

    def set_keyword(self, keyword):
        """
        搜索框输入关键字
        :return:
        """
        self.send_keys(self.keyword_loc, keyword)

    def search(self):
        """
        点击搜索按钮
        :return:
        """
        self.click(self.search_loc)


if __name__ == '__main__':
    driver = mydriver.browser()
    baidu = BaiduPage(driver)
    baidu.open_browser(baidu.url)
    baidu.set_keyword('selenium')
    time.sleep(1)
    baidu.search()
    time.sleep(1)
    baidu.scroll_to_buttom()
    time.sleep(3)
    baidu.scroll_to_top()
    time.sleep(2)
    baidu.close_browser()

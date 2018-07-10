#!/usr/bin/env python3
# coding:utf-8

import os


class BasePage(object):
    """所有页面的基类，定义页面相关通用方法"""

    def __init__(self, driver):
        """
        初始化获取driver
        """
        self.driver = driver

    def find_element(self, *loc):
        """
        查找一个元素
        :return: 定位的元素
        """
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        查找一组元素
        :return: 定位的元素组
        """
        return self.driver.find_elements(*loc)

    def open_browser(self, url):
        """
        启动浏览器，跳转到指定url
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def page_url(self):
        """
        当前页面的url
        :return: 当前页面的url
        """
        return self.driver.current_url

    def page_title(self):
        """
        当前页面的title
        :return: 当前页面的title
        """
        return self.driver.title

    def click(self, loc):
        """
        点击某个元素
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except AttributeError:
            print("未找到%s" % loc)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        """
        输入框输入字符
        :return:
        """
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("未找到%s" % loc)

    def script(self, js):
        """
        执行js脚本
        :return:
        """
        self.driver.execute_script(js)

    def scroll_to_top(self):
        """
        页面滚动到顶部
        :return:
        """
        self.script('window.scrollTo(0,0);')

    def scroll_to_buttom(self):
        """
        页面滚动到底部
        :return:
        """
        self.script('window.scrollTo(0,document.body.scrollHeight);')

    def screenshot(self, picture_name):
        """
        页面截图
        :return:
        """
        current_path = os.path.dirname(os.path.realpath(__file__))
        screenshot_path = os.path.join(os.path.dirname(current_path), r'Report\Screenshot')
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)

        picture_path = os.path.join(screenshot_path, picture_name)
        self.driver.get_screenshot_as_file(picture_path)

    def enter_frame(self, loc):
        """
        进入frame
        :return:
        """
        frame = self.find_element(*loc)
        self.driver.switch_to_frame(frame)

    def exit_frame(self):
        """
        退出frame
        :return:
        """
        self.driver.switch_to_default_content()

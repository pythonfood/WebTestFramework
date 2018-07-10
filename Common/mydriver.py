#!/usr/bin/env python3
# coding:utf-8

import time
from selenium import webdriver
from Config.readConfig import ReadConfig

readconfig = ReadConfig()


def browser(browser_name=readconfig.browser('browser')):
    """
    指定驱动的浏览器类型
    :return: driver
    """

    if browser_name == 'ie':
        driver = webdriver.Ie()
        return driver
    elif browser_name == 'edge':
        driver = webdriver.Edge()
        return driver
    elif browser_name == 'chrome':
        # options = webdriver.ChromeOptions()
        # options.add_argument('--user-data-dir=C:\\Users\\tester\\AppData\\Local\\Google\\Chrome\\User Data')
        # dr = webdriver.Chrome(chrome_options=options)
        driver = webdriver.Chrome()
        return driver
    elif browser_name == 'firefox':
        # profile = webdriver.FirefoxProfile('C:\\Users\\tester\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\h56tugrr.selenium')
        # dr = webdriver.Firefox(profile)
        driver = webdriver.Firefox()
        return driver
    else:
        print('不支持这个浏览器')


if __name__ == '__main__':
    dr = browser()
    dr.implicitly_wait(15)
    dr.get('https://www.baidu.com')
    dr.find_element_by_id("kw").send_keys("selenium")
    time.sleep(1)
    dr.find_element_by_id("su").click()
    time.sleep(3)
    js = "window.scrollTo(100,500);"
    dr.execute_script(js)
    time.sleep(2)
    dr.quit()

# !/usr/bin/env python3
# coding:utf-8

import unittest
import time
from parameterized import parameterized
from Common import mydriver
from Common.mylog import MyLog
from TestData import testdata
from PageObject.baidu_page import BaiduPage

mylog = MyLog().mylog()
test_data = testdata.read_data('test_search_keyword.xlsx', '搜索关键字')[1:]  # 测试数据，去除首行字段行


def testcase_name(testcase_func, param_num, param):
    """
    设置测试用例名称，便于在测试报告中展示
    注：修改了parameterized的源代码，测试用例名称中可以用中文

    :param testcase_func: 测试方法名称
    :param param_num: 参数序号
    :param param: 传入参数
    :return: 格式化后的用例名称
    """
    return "%s_%s" % (
        testcase_func.__name__,
        parameterized.to_safe_name(str(param_num) + '_' + str(param.args[0])),
    )


class TestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.baidu.com'
        self.driver = mydriver.browser()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    @parameterized.expand(test_data, testcase_func_name=testcase_name)  # 调用数据的传参必须和数据一一对应
    def test_search_keyword(self, case_name, keyword, generate_data, token):
        mylog.info('Run test case:{}'.format(self._testMethodName))
        print('\n【Step】')

        baidu = BaiduPage(self.driver)
        print('* 打开url:', self.url)
        mylog.info('* 打开url:{}'.format(self.url))
        baidu.open_browser(self.url)

        print('* 输入keyword:', keyword)
        mylog.info('* 输入keyword:{}'.format(keyword))
        baidu.set_keyword(keyword)
        time.sleep(1)

        baidu.search()
        mylog.info('* 点击搜索按钮')
        print('* 点击搜索按钮')
        time.sleep(5)

        picture_name = self._testMethodName + '.png'
        print('* 页面截图:', picture_name)
        mylog.info('* 页面截图:{}'.format(picture_name))
        baidu.screenshot(picture_name)

        print('【Expect】')

        print('* 页面title:', keyword+'_百度搜索')
        mylog.info('* 期望页面title:{},实际页面title:{}。'.format(keyword+'_百度搜索', baidu.page_title()))
        self.assertRegex(baidu.page_title(), keyword+'_百度搜索')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Pycharm执行时注意：鼠标需要放在unittest.main(verbosity=2)代码块的位置，否则会报错

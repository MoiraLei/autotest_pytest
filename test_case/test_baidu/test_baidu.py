# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/7
@Auth ： qihang
"""

from common.request_tool import RequestTool
from common.read_config import ReadConfig
import time

url = 'http://baidu.com'


class TestBaiDu:

    def test_serch(self):
        print("test_search3")
        driver = RequestTool()
        ipconfig = ReadConfig().get_http('baseurl')

        driver.open_url(ipconfig)


        driver.find_element('id', 'kw').send_keys('哈哈2')
        time.sleep(2)
        driver.click('id', 'su')

        time.sleep(2)
        driver.get_screenshot(2)
        driver.delete_self()

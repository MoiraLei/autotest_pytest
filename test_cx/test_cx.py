# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/7
@Auth ： qihang
"""

import pytest
import requests

url = 'http://baidu.com'
datas = [{'case', '哈哈1'}, {'case', '哈哈2'}]


class TestCx:
    # 参数传递
    # @pytest.mark.parametrize('item', datas)
    # def test_01(self, item):
    #     print(item)

    # 该测试类---有个前置的操作（初始化）
    def setup_class(self):
        print("执行测试类之前，我需要执行操作")

    def teardown(self):
        print("------该测试类的环境清除-----")

    def test_search1(self):
        data = "哈哈1"
        r = requests.get(url, data)
        assert (r.status_code == 200)

    def test_search2(self):
        data = "哈哈2"
        r = requests.get(url, data)
        assert (r.status_code == 200)

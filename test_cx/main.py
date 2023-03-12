# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/12
@Auth ： qihang
"""
import pytest
import os

if __name__ == "__main__":
    # 需要打印对应的信息，需要在列表里面加-s
    # 1:--alluredir ---生成临时文件，测试用例的结果数据放到目录   --alluredir   存放目录
    pytest.main(["-s", "--alluredir", "../reports/tmp", "test_cx.py::TestCx::test_search2"])
    # 通过--alluredir把allure需要的数据存到../report/tmp这个路径下面
    # ../--所在路径的父级别目录是test_case的目录隔壁邻居report文件下tmp，专门放alluer报告生成的需要的数据源

    os.system("allure generate ../reports/tmp -o ../reports/report --clean")

    # 2:临时数据没有报告的，allure generate allure才会生成报告   -----allure生成器生成allure报告--generate allure生成器,cmd指令
    # 需要os模块os.system()调用指令可以在local的cmd里面敲
    # os.system("allure generate 报告需要的数据 -o 报告存放目录 --clean")
    # -o生成
    # allure generate生成报告指令，把../report/tmp 的文件-o生成报告out out一下，生成的报告放在../report/report
    # --clean把上次报告清除一下用--clean
    # allure报告生成的是一个服务，（本地服务）和jinkins结合，放在整个里面去集成，放到公共服务器里面

    # pytest.main()
    # pytest.main(['test_cx.py::TestCx::test_search2'])
    # pytest.main(['-s', '-v', '--html=./test.html', 'test_cx.py::TestCx::test_search2'])

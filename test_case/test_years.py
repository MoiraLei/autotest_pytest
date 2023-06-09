# -*-coding:utf-8-*-

import sys

sys.path.append(".")


def is_leap_year(year):
    # 先判断year是不是整型
    if isinstance(year, int) is not True:
        raise TypeError("传入的年份参数不是整数")
    elif year <= 0:
        raise ValueError("公元元年是从公元纪年开始算起！")
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("%d年是闰年" % year)
        return True
    else:
        print("%d年不是闰年" % year)
        return False


import pytest


class TestYear:
    def test_some_exception(self):
        with pytest.raises(ValueError) as ex:
            is_leap_year(-1)

        assert "从公元纪年开始" in str(ex.value)
        assert ex.type == ValueError

    def test_some_exception2(self):
        with pytest.raises(TypeError) as ex:
            is_leap_year(0.1)

        assert "传入的年份参数不是整数" in str(ex.value)
        assert ex.type == TypeError

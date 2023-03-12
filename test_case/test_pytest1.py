#!/usr/bin/env python
# -*-coding:utf-8-*-
import pytest


def func(x):
    return x + 1

def test_answer1():
    assert func(4) == 5

def test_answer2():
    assert func(3) == 5

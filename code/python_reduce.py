# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:13 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_reduce.py
# @Software: PyCharm

""" reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算 """

from functools import reduce


def add(x, y):
    return x + y


if __name__ == '__main__':
    print(reduce(add, list(range(1, 101))))  # 从 1 加到 100

# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:11 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_map.py
# @Software: PyCharm


""" map 把一个可迭代对象中的每一个元素与一个函数执行后返回一个执行后的可迭代对象 """


def func(x):
    return x + 10


list_result = list(map(func, [1, 2, 3, 4]))
tuple_result = tuple(map(func, (1, 2, 3, 4)))
generator_result = (i for i in list(map(func, [1, 2, 3, 4])))


if __name__ == '__main__':
    print(list_result)
    print(tuple_result)
    print(generator_result)
    print(next(generator_result))
    print(next(generator_result))
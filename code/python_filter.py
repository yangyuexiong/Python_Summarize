# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:14 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_filter.py
# @Software: PyCharm

""" filter 把一个可迭代对象中的每一个元素与一个函数执行后返回True的元素放在一个可迭代最新中 """


def is_delete(n):
    if isinstance(n, dict):
        if n.get('status') == '正常':
            return n
    else:
        return n


student = [
    {"id": 1, "status": "正常"},
    {"id": 2, "status": "正常"},
    {"id": 3, "status": "不正常"},
    {"id": 4, "status": "正常"},
    '测试1',
    '测试2',
    '测试3'
]

list_result = list(filter(is_delete, student))
tuple_result = tuple(filter(is_delete, student))
generator_result = (i for i in list(filter(is_delete, student)))

if __name__ == '__main__':
    print(list_result)
    print(tuple_result)
    print(generator_result)
    print(next(generator_result))
    print(next(generator_result))

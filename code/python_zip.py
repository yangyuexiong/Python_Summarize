# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 3:32 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_zip.py
# @Software: PyCharm


l1 = ["a", "b", "c"]
l2 = ["1", "2", "3"]

list_result = list(zip(l1, l2))
dict_result = dict(zip(l1, l2))
tuple_result = tuple(zip(l1, l2))

if __name__ == '__main__':
    print(list_result)
    print(dict_result)
    print(tuple_result)

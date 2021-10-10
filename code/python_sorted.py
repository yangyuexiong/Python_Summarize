# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:17 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_sorted.py
# @Software: PyCharm

""" sorted 排序 """

array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
array1 = sorted(array, key=lambda x: x["age"])
array2 = sorted(array, key=lambda x: x["age"], reverse=True)

if __name__ == '__main__':
    print(array1)
    print(array2)

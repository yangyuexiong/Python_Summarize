# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:19 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_product.py
# @Software: PyCharm

""" product 笛卡尔积 """

import sys
import itertools

list1 = [1, 2, 3]
list2 = [11, 22, 33, 44]
list3 = [111, 222, 333, 444, 555, 666]
ll = [list1, list2, list3]

list_result = [i for i in itertools.product(*ll)]  # list
generator_result = (i for i in itertools.product(*ll))  # generator

if __name__ == '__main__':
    # 内存打印对比
    print(list_result)
    print(generator_result)
    print(next(generator_result))
    print(next(generator_result))
    print(sys.getsizeof(list1))
    print(sys.getsizeof(list2))
    print(sys.getsizeof(list3))
    print(sys.getsizeof(list_result))
    print(sys.getsizeof(generator_result))

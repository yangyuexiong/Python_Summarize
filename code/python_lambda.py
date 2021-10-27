# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 3:29 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_lambda.py
# @Software: PyCharm


list_result1 = list(map(lambda x: x + x, [1, 2, 3, 4]))
list_result2 = list(map(lambda x: {x: x}, [1, 2, 3, 4]))

if __name__ == '__main__':
    print(list_result1)
    print(list_result2)

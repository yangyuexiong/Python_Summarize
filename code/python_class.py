# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:24 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_class.py
# @Software: PyCharm


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 动态创建类

if __name__ == '__main__':
    h = Hello()
    h.hello()


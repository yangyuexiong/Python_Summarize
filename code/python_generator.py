# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:23 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : python_generator.py
# @Software: PyCharm


"""
yield:

yield form: 后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，对比yield来说代码更加简洁

send:

"""
from collections.abc import Iterable, Iterator
from inspect import isgeneratorfunction


def gen_test_1():
    yield "yyx1"
    yield "yyx2"
    yield "yyx3"


def gen_test_2():
    yield from ['user1', {"a": "b"}, (99, 88)]
    yield from "abcd"


def test_3():
    pass


gen_1 = gen_test_1()
gen_2 = gen_test_2()

test1 = iter([1, 2, 3])
test2 = [1, 2, 3]

print(isinstance(test1, Iterable))  # 判断是否是一个可迭代对象
print(isinstance(test1, Iterator))  # 判断是否是一个迭代器-方法1
print(hasattr(test1, "__next__"))  # 判断是否是一个迭代器-方法2
print('-' * 33)
print(isinstance(test2, Iterable))
print(isinstance(test2, Iterator))
print(hasattr(test2, "__next__"))
print('-' * 33)
print(isgeneratorfunction(gen_test_1))  # 判断函数是否是一个生成器函数
print(isgeneratorfunction(test_3))

if __name__ == '__main__':
    print('=== gen_1 ===')
    print(type(gen_1))
    print(next(gen_1))
    print(next(gen_1))
    print(next(gen_1))

    print('=== gen_2 ===')
    print(type(gen_2))
    print(next(gen_2))
    print(next(gen_2))
    print(next(gen_2))
    print(next(gen_2))

    print(next(test1))
    print(test1.__next__())

    try:
        print(next(test2))  # 非迭代器或生成器函数调用next()
        t3 = test_3()
        print(next(t3))
    except BaseException as e:
        print(str(e))

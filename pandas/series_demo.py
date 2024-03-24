import pandas as pd
import numpy as np


"""
    1.如果使用字典，则字典的key会成为索引，注意索引的顺序，不同的python版本不一样
    a    1
    b    2
    c    4
    dtype: int64
"""
def series_demo1():
    s = pd.Series({'a': 1, 'b': 2, 'c': 4})
    print(s)

"""
    2.数组或多维数组
"""
def series_demo2():

    """
        0    0.006110
        1    1.635467
        2   -0.148324
        3    0.467240
        4    0.032786
        5    0.676378
        6    0.335271
        7   -0.560542
        8   -1.032763
        9    0.008987
        dtype: float64
    """
    s = pd.Series(np.random.randn(10))
    print(s)

    """
        0    1
        1    2
        2    3
        3    4
        4    5
        dtype: int64
    """
    s = pd.Series([1,2,3,4,5])
    print(s)

    """
        index长度必须与data长度保持一致，如果不指定index，则会使用数值型索引
        a    20
        b    39
        c    44
        d    10
        e    16
        dtype: int64
    """
    s = pd.Series(np.random.randint(10, 100, 5), index=['a', 'b', 'c', 'd', 'e'])
    print(s)

    """
        0    [1, 2]
        1    [3, 4]
        2    [5, 6]
        dtype: object
    """
    s = pd.Series([[1,2], [3,4], [5,6]])
    print(s)

"""
    3.标量值
    1    a
    2    a
    3    a
    dtype: object
"""
def series_demo3():
    s = pd.Series('a', index=[1, 2, 3])
    print(s)

"""
    Series 是带标签的一维数组，可存储整数、浮点数、字符串、Python 对象等类型的数据。轴标签统称为索引。调用 pd.Series 函数即可创建 Series：
    data支持的数据类型：
        字典
        多维数组
        标量值 如 5
"""
if __name__ == '__main__':
    # series_demo1()
    # series_demo2()
    series_demo3()

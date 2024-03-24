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
    #Series 类似固定大小的字典，可以用索引标签提取值或设置值：
    print(s[0])

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
    print(s.array)
    #Series 只是类似于多维数组，提取真正的多维数组，要用 Series.to_numpy()
    print(s.to_numpy())
    #Series 类似固定大小的字典，可以用索引标签提取值或设置值：
    print(s[1])
    #引用 Series 里没有的标签会触发异常：
    # print(s[10])
    #get 方法可以提取 Series 里没有的标签，返回 None 或指定默认值：
    print(s.get(10))


"""
    Series 和 NumPy 数组一样，都不用循环每个值，而且 Series 支持大多数 NumPy 多维数组的方法。
"""
def series_demo4():
    """
        0    1.342951
        1    0.548485
        2    0.615303
        3   -0.674434
        4   -1.889594
        5    0.570270
        6   -1.703388
        7   -0.689749
        8   -0.596892
        9   -0.640786
        dtype: float64
    """
    s = pd.Series(np.random.randn(10))
    print(s)
    """
        0    2.685903
        1    1.096971
        2    1.230606
        3   -1.348867
        4   -3.779188
        5    1.140541
        6   -3.406776
        7   -1.379497
        8   -1.193783
        9   -1.281573
        dtype: float64
    """
    print(s * 2)

    """
        0    2.020905
        1    1.656544
        2   -0.837441
        3    0.824724
        4    0.604664
        5   -0.290922
        6    0.567647
        7    0.530125
        8    1.894911
        9    1.616971
        dtype: float64
    """
    print(s + 1)


def series_demo5():
    s = pd.Series(np.random.randint(10, 100, 5), index=['a', 'b', 'c', 'd', 'e'],name="firstname")
    """
        a    97
        b    72
        c    60
        d    55
        e    88
        dtype: int64
    """
    print(s)
    """
        b    72
        c    60
        d    55
        e    88
        dtype: int64
    """
    print(s[1:])
    """
        a    97
        b    72
        c    60
        d    55
        dtype: int64
    """
    print(s[:-1])
    """
        a      NaN
        b    144.0
        c    120.0
        d    110.0
        e      NaN
        dtype: float64
        
        Series 和多维数组的主要区别在于， Series 之间的操作会自动基于标签对齐数据。因此，不用顾及执行计算操作的 Series 是否有相同的标签。
        操作未对齐索引的 Series， 其计算结果是所有涉及索引的并集。
        如果在 Series 里找不到标签，运算结果标记为 NaN，即缺失值。
        编写无需显式对齐数据的代码，给交互数据分析和研究提供了巨大的自由度和灵活性。
        Pandas 数据结构集成的数据对齐功能，是 Pandas 区别于大多数标签型数据处理工具的重要特性。
    """
    s1 = (s[1:] + s[:-1])
    print(s1)
    """
        b    144.0
        c    120.0
        d    110.0
        dtype: float64
        
        总之，让不同索引对象操作的默认结果生成索引并集，是为了避免信息丢失。就算缺失了数据，索引标签依然包含计算的重要信息。
        当然，也可以用**dropna** 函数清除含有缺失值的标签。
    """
    print(s1.dropna())
    print(s1.name)

    s1 = s1.rename('hahaha')
    print(s1)
    print(s1.name)


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
    # series_demo3(
    # series_demo4()
    series_demo5()

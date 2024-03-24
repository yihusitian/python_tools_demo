"""
    DataFrame 是由多种类型的列构成的二维标签数据结构，类似于 Excel 、SQL 表，或 Series 对象构成的字典。
    DataFrame 是最常用的 Pandas 对象，与 Series 一样，DataFrame 支持多种类型的输入数据：
        一维 ndarray、列表、字典、Series 字典
        二维 numpy.ndarray
    除了数据，还可以有选择地传递 index（行标签）和 columns（列标签）参数。
    传递了索引或列，就可以确保生成的 DataFrame 里包含索引或列。
    Series 字典加上指定索引时，会丢弃与传递的索引不匹配的所有数据。
"""
import pandas as pd
import numpy as np

"""
    用 Series 字典或字典生成 DataFrame
"""
def demo1():
    data = {"onecol": pd.Series([1,2,3,4], index=['a','b','c','d']),
            "secondcol": pd.Series([2,4,6,8,10], index=['a','b','c','d','e']),}
    df = pd.DataFrame(data)
    """
           onecol  secondcol
        a     1.0          2
        b     2.0          4
        c     3.0          6
        d     4.0          8
        e     NaN         10
    """
    print(df)

    """
        创建dataframe指定索引
           onecol  secondcol
        b     2.0          4
        c     3.0          6
        e     NaN         10

    """
    df = pd.DataFrame(data, index=['b', 'c', 'e'])
    print(df)

    """
        创建dataframe指定索引和列
           onecol threecol
        b     2.0      NaN
        c     3.0      NaN
        e     NaN      NaN
        
        index 和 columns 属性分别用于访问行、列标签：
        指定列与数据字典一起传递时，传递的列会覆盖字典的键。
    """
    df = pd.DataFrame(data, index=['b', 'c', 'e'], columns=['onecol', 'threecol'])
    print(df)
    """
        Index(['b', 'c', 'e'], dtype='object')
    """
    print(df.index)
    """
        Index(['onecol', 'threecol'], dtype='object')   
    """
    print(df.columns)

"""
    用多维数组字典、列表字典生成 DataFrame
    多维数组的长度必须相同。如果传递了索引参数，index 的长度必须与数组一致。
                        如果没有传递索引参数，生成的结果是 range(n)，n 为数组长度。
"""
def demo2():
    data = {"one": [0,2,3,4],
            "two": [1,2,3,5]}
    df = pd.DataFrame(data)
    """
           one  two
        0    0    1
        1    2    2
        2    3    3
        3    4    5
    """
    print(df)
    df = pd.DataFrame(data, index=['a','b','c','d'])
    """
       one  two
    a    0    1
    b    2    2
    c    3    3
    d    4    5
    """
    print(df)


"""
    用结构多维数组或记录多维数组生成 DataFrame
    如下使用元组构建dataframe
"""
def demo3():
    data = [(1,2,3,'hello'), (10, 20, 40, 'world')]
    df = pd.DataFrame(data)
    """
            0   1   2      3
        0   1   2   3  hello
        1  10  20  40  world
    """
    print(df)

    """
           0  1  2       3
        0  1  2  3  hahaha
        1  2  3  4    None
        每个元组就相当于一行数据
    """
    data = [(1,2,3,'hahaha'), (2,3,4)]
    df = pd.DataFrame(data)
    print(df)

    """
        显式指定索引
           0  1  2       3
        a  1  2  3  hahaha
        b  2  3  4    None
    """
    df = pd.DataFrame(data, index=['a','b'])
    print(df)

    """
        指定索引和列
           one  two  three    four
        a    1    2      3  hahaha
        b    2    3      4    None
    """
    df = pd.DataFrame(data, index=['a','b'], columns=['one', 'two','three','four'])
    print(df)


"""
    用列表字典生成 DataFrame
"""
def demo4():
    """
            a   b     c
        0   1   2   NaN
        1  10  20  30.0
    """
    data = [{'a': 1, 'b': 2}, {'a': 10, 'b': 20, 'c': 30}]
    df = pd.DataFrame(data)
    print(df)

    """
        指定索引
             a   b     c
        aa   1   2   NaN
        bb  10  20  30.0
    """
    df = pd.DataFrame(data, index=['aa', 'bb'])
    print(df)


"""
    用元组字典生成 DataFrame
    元组字典可以自动创建多层索引 DataFrame。
"""
def demo5():
    """
           a              b
           b    a    c    a     b
    A B  1.0  4.0  5.0  8.0  10.0
      C  2.0  3.0  6.0  7.0   NaN
      D  NaN  NaN  NaN  NaN   9.0


    """
    data = {('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                  ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                  ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                  ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                  ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}}
    df = pd.DataFrame(data)
    print(df)


"""
    提取、添加、删除列
    DataFrame 就像带索引的 Series 字典，提取、设置、删除列的操作与字典类似：
"""
def demo6():
    data = {'one': pd.Series([1,2,3,4]), 'two': pd.Series([3,4,5,6])}
    df = pd.DataFrame(data)
    """
           one  two
        0    1    3
        1    2    4
        2    3    5
        3    4    6
    """
    print(df)
    """
       one  two  three
    0    1    3      3
    1    2    4      8
    2    3    5     15
    3    4    6     24
    """
    df['three'] = df['one'] * df['two']
    print(df)
    """
           one  two  three   flag
        0    1    3      3  False
        1    2    4      8  False
        2    3    5     15   True
        3    4    6     24   True
    """
    df['flag'] = df['three'] > 10
    print(df)
    del df['two']
    """
           one  three   flag
        0    1      3  False
        1    2      8  False
        2    3     15   True
        3    4     24   True
    """
    print(df)
    # df = df.pop('three')
    """
        0     3
        1     8
        2    15
        3    24
        Name: three, dtype: int64
    """
    # print(df)

    """
        填充标量值
           one  three   flag  four
        0    1      3  False  four
        1    2      8  False  four
        2    3     15   True  four
        3    4     24   True  four
    """
    df['four'] = 'four'
    print(df)

    """
        插入与 DataFrame 索引不同的 Series 时，以 DataFrame 的索引为准：
           one  three   flag  four  five
        0    1      3  False  four   1.0
        1    2      8  False  four   2.0
        2    3     15   True  four   NaN
        3    4     24   True  four   NaN
    """
    df['five'] = df['one'][0:2]
    print(df)

    """
        在第三列插入一新列，与第三列一致
           one  three   flag  new_col  four  five
        0    1      3  False    False  four   1.0
        1    2      8  False    False  four   2.0
        2    3     15   True     True  four   NaN
        3    4     24   True     True  four   NaN
    """
    df.insert(3, 'new_col', df['flag'])
    print(df)

"""
    从 3.6 版开始，Python 可以保存 **kwargs 顺序。这种操作允许依赖赋值，**kwargs 后的表达式，可以引用同一个 assign() 函数里之前创建的列 。
"""
def demo7():
    df = pd.DataFrame({'a':[1,2,3,4], 'b':[20,30,40,50]})
    """
           a   b
        0  1  20
        1  2  30
        2  3  40
        3  4  50
    """
    print(df)
    """
           a   b   c    d
        0  1  20  21   20
        1  2  30  32   60
        2  3  40  43  120
        3  4  50  54  200
    """
    df = df.assign(c=lambda x: x['a'] + x['b'],
                   d=lambda x: x['a'] * x['b'])
    print(df)

"""
    索引 / 选择

"""
def demo8():
    df = pd.DataFrame({'a':[1,2,3,4], 'b':[20,30,40,50], 'c':[120,130,140,150]}, index=['i0','i1','i2','i3'])
    """
            a   b    c
        i0  1  20  120
        i1  2  30  130
        i2  3  40  140
        i3  4  50  150
    """
    print(df)

    """
        选择列	df[col] 返回Series
        i0    1
        i1    2
        i2    3
        i3    4
        Name: a, dtype: int64
    """
    print(df['a'])

    """
        a      1
        b     20
        c    120
        Name: i0, dtype: int64
        用标签选择行	df.loc[label]	Series   
    """
    print(df.loc['i0'])

    """
        用整数位置选择行	df.iloc[loc]	Series
        a      2
        b     30
        c    130
        Name: i1, dtype: int64
    """
    print(df.iloc[1])

    """
        行切片	df[5:10]	DataFrame
            a   b    c
        i0  1  20  120
        i1  2  30  130
    """
    print(df[0:2])

"""
    数据对齐和运算
    DataFrame 对象可以自动对齐**列与索引（行标签）**的数据。与上文一样，生成的结果是列和行标签的并集。
"""
def demo9():
    """
            A         B         C         D
        0 -0.235710 -0.851859 -0.539240  0.242715
        1  1.389218 -0.095200  0.757678  0.524310
        2 -0.940931  1.244458 -1.138388 -1.142569
        3  0.341460  0.441990 -0.657604 -0.077982
        4 -0.448077 -1.007870  1.198693  0.270749
        5 -0.038532 -1.306194 -0.356251 -1.037278
        6 -0.775786  0.289110  1.121652  0.656815
        7 -0.289698 -0.757507  0.543596  0.609986
        8 -0.450732 -0.466666 -0.069487  0.828844
        9  1.869199  1.662720 -0.442234  0.886285
    """
    df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
    print(df)
    df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
    """
              A         B         C
        0 -0.274047 -0.187781 -0.735651
        1 -0.849969  0.594793 -0.062036
        2 -0.121091 -0.131691 -0.933380
        3 -0.263778 -0.134752  0.946925
        4 -1.308507  0.936733 -0.606326
        5  0.837404 -0.167474  0.072241
        6 -1.739721 -0.714655  0.616265
    """
    print(df2)

    """
              A         B         C   D
        0 -0.509756 -1.039639 -1.274891 NaN
        1  0.539248  0.499594  0.695643 NaN
        2 -1.062022  1.112767 -2.071768 NaN
        3  0.077682  0.307238  0.289321 NaN
        4 -1.756584 -0.071137  0.592368 NaN
        5  0.798872 -1.473668 -0.284010 NaN
        6 -2.515507 -0.425545  1.737917 NaN
        7       NaN       NaN       NaN NaN
        8       NaN       NaN       NaN NaN
        9       NaN       NaN       NaN NaN
    """
    df3 = df + df2
    print(df3)

    """
        DataFrame 和 Series 之间执行操作时，默认操作是在 DataFrame 的列上对齐 Series 的索引，按行执行广播操作。
    """
    df4 = df - df.iloc[0]
    print(df4)

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    # demo8()
    demo9()
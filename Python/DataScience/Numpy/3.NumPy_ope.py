import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#数组的运算

##数据与标量的运算
array1 = np.arange(1, 10)
print(array1 + 10)
print(array1 * 10)
print(array1 > 5)
print(array1 % 2 == 0)

##数组与数组的运算
array2 = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])
print(array1 + array2)
print(array1 * array2)
print(array1 ** array2)

##通用一元函数
print(np.sqrt(array1))#开方
print(np.log2(array1))#对数
print(np.sin(array1))#三角函数
print(np.abs(array1))#绝对值

##通用二元函数
array3 = np.array([[4, 5, 6], [7, 8, 9]])
array4 = np.array([[1, 2, 3], [3, 2, 1]])
print(np.maximum(array3, array4))#对应位置取最大值
print(np.power(array3, array4))#对应位置取幂

##数组的广播
array5 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
array6 = np.array([1, 2, 3])
array5 + array6
array7 = np.array([[1], [2], [3], [4]])
array5 + array7


'''
其他常用函数
表3：NumPy其他常用函数

函数            说明
unique          去除数组重复元素，返回唯一元素构成的有序数组
copy            返回拷贝数组得到的数组
sort            返回数组元素排序后的拷贝
split / hsplit / vsplit  将数组拆成若干个子数组
stack / hstack / vstack  将多个数组堆叠成新数组
concatenate     沿着指定的轴连接多个数组构成新数组
append / insert 向数组末尾追加元素 / 在数组指定位置插入元素
argwhere        找出数组中非0元素的位置
extract / select / where 按照指定的条件从数组中抽取或处理数组元素
flip            沿指定的轴翻转数组中的元素
fromregex       通过读取文件和正则表达式解析获取数据创建数组对象
repeat / tile   通过对元素的重复来创建新数组
roll            沿指定轴对数组元素进行移位
resize          重新调整数组的大小
place / put     将数组中满足条件的元素/指定的元素替换为指定的值
partition       用选定的元素对数组进行一次划分并返回划分后的数组
'''
np.unique(array5)
array8 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
array9 = np.array([[4, 4, 4], [5, 5, 5], [6, 6, 6]])
np.hstack((array8, array9))
np.vstack((array8, array9))
np.concatenate((array8, array9))
np.concatenate((array8, array9), axis=1)
np.append(array1, [10, 100])
np.insert(array1, 1, [98, 99, 100])
np.extract(array1 % 2 != 0, array1)
np.select([array1 <= 3, array1 >= 7], [array1 * 10, array1 ** 2])
np.where(array1 <= 5, array1 * 10, array1 ** 2)
np.repeat(array1, 3)
np.tile(array1, 2)
np.resize(array1, (5, 3))
np.resize(array5, (2, 4))
np.put(array1, [0, 1, -1, 3, 5], [100, 200])
array1
np.place(array1, array1 > 5, [1, 2, 3])
array1
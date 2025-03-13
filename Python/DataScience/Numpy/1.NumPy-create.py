import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#创建数组对象
##创建一维数组array
array1 = np.array([1, 2, 3, 4, 5])
array1
array2 = np.array([[1, 2, 3], [4, 5, 6]])
array2
##创建等差数组array
array3 = np.arange(0, 20, 2)
array3
##创建等间隔数组linspace
array4 = np.linspace(-1, 1, 11)
array4
##创建等比数组logspace
array5 = np.logspace(1, 10, num=10, base=2)
array5
##从字符串创建数组fromstring
"""
参数解析：
'1, 2, 3, 4, 5'（字符串）：

这是输入数据，以字符串的形式提供，包含逗号分隔的数字。
sep=','（分隔符）：

指定字符串中的数值是用 ,（逗号） 进行分隔的。
sep 代表分隔符，如果 sep=''（默认值），那么 fromstring 会尝试按照二进制方式解析字符串，而不是文本数据。
dtype='i8'（数据类型）：

指定返回数组的元素数据类型。
'i8' 代表 64 位整数(int64)即 numpy.int64 类型。
你可以换成 'f8'(float64)表示返回 float64 类型的数组。
"""
array6 = np.fromstring('1, 2, 3, 4, 5', sep=',', dtype='i8')
array6 = np.array('1, 2, 3, 4, 5'.split(','), dtype='i8')
array6
##从生成器创建数组fromiter
def fib(how_many):
    a, b = 0, 1  # 初始化前两个斐波那契数
    for _ in range(how_many):  # 运行 how_many 次
        a, b = b, a + b  # 计算下一个斐波那契数
        yield a  # 使用 yield 生成数列的下一个数
gen = fib(20)
array7 = np.fromiter(gen, dtype='i8')
array7
'''
yield 关键字的作用
yield 是 Python 生成器(generator)的关键字，
用于在函数中 逐步生成值，而不是一次性返回整个结果。

与 return 的区别
return:函数执行到 return 语句时，会返回值并终止函数。
yield:函数执行到 yield 时，会返回值，
但不会终止函数，而是暂停，下次调用时从暂停的位置继续执行。
'''
##使用numpy.random模块生成随机数组
array8 = np.random.rand(10)
array8
###生成随机整数数组[1,100)
array9 = np.random.randint(1, 100, 10)
array9
###生成随机正态分布数组
array10 = np.random.normal(50, 10, 20)
array10
###生成随机二维数组3*4
array11 = np.random.rand(3, 4)
array11
###生成随机三维数组3*4*5
array12 = np.random.randint(1, 100, (3, 4, 5))
array12
'''
randint 生成指定范围内的随机整数，包括上下限。
random.randint(a, b): 生成一个介于 a 和 b 之间的整数，包含 a 和 b。
返回值类型:整数(int)。
rand 生成 [0, 1) 之间的随机浮点数，不接受范围参数。
只返回一个0.0 ≤ 结果 < 1.0 的浮点数。
无法直接指定范围，如果需要特定范围的随机数，可以手动调整：
num = random.random() * 100  # 生成 0~100 之间的随机浮点数
'''
##zeros函数创建全零数组
array13 = np.zeros((3, 4))
array13
##ones函数创建全1数组
array14 = np.ones((3, 4))
array14
##full函数创建未初始化数组
array15 = np.full((3, 4), 10)
array15
##eye函数创建单位矩阵
np.eye(4)
##读取图片文件创建数组
array16 = plt.imread(r'Python\DataScience\guido.jpg')
array16


#数组对象的属性
##size:数组元素个数
array17 = np.arange(1, 100, 2)
array18 = np.random.rand(3, 4)
print(array16.size)
print(array17.size)
print(array18.size)
##shape:数组形状
print(array16.shape)
print(array17.shape)
print(array18.shape)
##dtype:数组元素数据类型
print(array16.dtype)
print(array17.dtype)
print(array18.dtype)
##ndim:数组维度
print(array16.ndim)
print(array17.ndim)
print(array18.ndim)
##itemsize:数组元素字节大小
print(array16.itemsize)
print(array17.itemsize)
print(array18.itemsize)
##nbytes:数组占用字节大小
print(array16.nbytes)
print(array17.nbytes)
print(array18.nbytes)

#数组的索引运算
##普通索引
array19 = np.arange(1, 10)
print(array19[0], array19[array19.size - 1])
array20 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array19[-array20.size], array19[-1])#array20.size 的值是 9,所以 -array20.size = -9。
array20[2]
print(array20[0][0])
print(array20[-1][-1])
array20[1][1] = 10
array20
array20[1] = [10, 11, 12]
array20
##切片索引
array20[:2, 1:]#切片索引是形如[开始索引:结束索引:跨度]的语法，其中开始索引包含在内，结束索引不包含在内。
array20[2, :]
array20[2:, :]
array20[:, :2]
array20[::2, ::2]
array20[::-2, ::-2]
##花式索引
array19[[0, 1, 1, -1, 4, -1]]
array20[[0, 2]]
array20[[0, 2], [1, 2]]
array20[[0, 2], 1]
##布尔索引
array19[[True, True, False, False, True, False, False, True, True]]
array19 > 5
array19[array19 > 5]
array19 % 2 == 0
(array19 > 5) & (array19 % 2 == 0)
array19[(array19 > 5) & (array19 % 2 == 0)]
'''
|运算符可以作用于两个布尔数组，
如果两个数组对应元素都是False，
那么运算的结果就是False，
否则就是True，
该运算符的运算规则类似于 Python 中的 or 运算符，
只不过作用的对象是两个布尔数组
'''
array21 = np.array([
    [1,  2,  3], 
    [4,  5,  6],  # `5` 在 (1,1)，符合 `array([1, 3, 5, 7, 9])`
    [7,  8,  9]
])
array20[array21 % 2 != 0]

##通过数组切片处理图像
guido_image = plt.imread(r'Python\DataScience\guido.jpg')#读取图片文件，imread 函数会返回一个包含图片像素数据的数组。
# 显示原始图像
plt.imshow(guido_image)
# 显示上下翻转的图像
plt.imshow(guido_image[::-1])
# 显示左右翻转的图像
plt.imshow(guido_image[:, ::-1])
# 显示裁剪后的图像
plt.imshow(guido_image[30:350, 90:300])
# 显示缩小后的图像
plt.imshow(guido_image[::10, ::10])

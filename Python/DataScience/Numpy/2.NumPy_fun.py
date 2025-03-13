import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#数组对象的方法
##获取描述统计信息
array1 = np.random.randint(1, 100, 10)
array1
print(array1.sum())  # 数组元素求和
print(np.sum(array1))  # 数组元素求和（使用 numpy 函数）
print(array1.mean())  # 数组元素求平均值
print(np.mean(array1))  # 数组元素求平均值（使用 numpy 函数）
print(np.median(array1))  # 数组元素求中位数
print(np.quantile(array1, 0.5))  # 数组元素求 50% 分位数（即中位数）

print(array1.max())  # 数组元素最大值
print(np.amax(array1))  # 数组元素最大值（使用 numpy 函数）
print(array1.min())  # 数组元素最小值
print(np.amin(array1))  # 数组元素最小值（使用 numpy 函数）
print(np.ptp(array1))  # 数组元素的极差（最大值与最小值之差）
    #numpy.ptp() 是 Peak-to-Peak(峰-峰值）函数，用于计算数组中 最大值与最小值 之间的差值。
q1, q3 = np.quantile(array1, [0.25, 0.75])  # 计算数组元素的 25% 和 75% 分位数
print(q3 - q1)  # 计算四分位距(75% 分位数与 25% 分位数之差）

# 计算 array1 的方差(Variance),即数据与均值的平方差的平均值
print(array1.var())  # 输出方差
print(np.var(array1))  # 使用 np.var() 计算方差，与 array1.var() 结果相同
# 计算 array1 的标准差(Standard Deviation),即方差的平方根
print(array1.std())  # 输出标准差
print(np.std(array1))  # 使用 np.std() 计算标准差，与 array1.std() 结果相同
# 计算变异系数(Coefficient of Variation, CV),衡量数据的相对离散程度
print(array1.std() / array1.mean())  # 标准差除以均值，表示数据的相对变化程度

#绘制箱线图
'''
箱线图又称为盒须图，
是显示一组数据分散情况的统计图，
因形状如箱子而得名。
它主要用于反映原始数据分布的特征，
还可以进行多组数据分布特征的比较。
'''
plt.boxplot(array1, showmeans=True)
plt.ylim([-20, 120])
plt.show()

'''
值得注意的是，
对于二维或更高维的数组，
在获取描述统计信息时，
可以通过名为axis的参数指定均值、方差等运算是沿着哪一个轴来执行，
axis参数不同,执行的结果可能是大相径庭的
'''
array2 = np.random.randint(60, 101, (5, 3))
array2
array2.mean()
array2.mean(axis=0)
array2.mean(axis=1)
array2.max(axis=0)
array2.max(axis=1)

plt.boxplot(array2, showmeans=True)  # 绘制 array2 的箱线图，并显示均值
plt.ylim([-20, 120])  # 设置 Y 轴的范围为 [-20, 120]
plt.show()  # 显示图像


'''
NumPy 的数组对象并没有提供计算几何平均值、调和平均值、去尾平均值等的方法，
如果有这方面的需求，
可以使用名为 scipy 的三方库，
它的stats模块中提供了这些函数。
此外，该模块还提供了计算众数、变异系数、偏态、峰度的函数
'''
from scipy import stats

print(np.mean(array1))                # 算术平均值
print(stats.gmean(array1))            # 几何平均值
print(stats.hmean(array1))            # 调和平均值
print(stats.tmean(array1, [10, 90]))  # 去尾平均值
print(stats.variation(array1))        # 变异系数
print(stats.skew(array1))             # 偏态系数
print(stats.kurtosis(array1))         # 峰度系数

'''
其他相关方法概述
all() / any()方法：判断数组是否所有元素都是True / 判断数组是否有为True的元素。

astype()方法：拷贝数组，并将数组中的元素转换为指定的类型。

reshape()方法：调整数组对象的形状。

dump()方法：保存数组到二进制文件中，可以通过 NumPy 中的load()函数从保存的文件中加载数据创建数组。
'''
array1 = np.array([1, 2, 3, 4, 5])  # 定义一个 NumPy 数组
array1.dump('array1-data')  # 将数组保存到文件 'array1-data'
array3 = np.load('array1-data', allow_pickle=True)
array3

array1.tofile('array.txt', sep=',')
array2.flatten()

array1.sort()
array1

array2.swapaxes(0, 1)

array2.transpose()

print(array2.tolist())
print(type(array2.tolist()))
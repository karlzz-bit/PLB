import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#向量

u = np.array([5, 1, 3])
m1 = np.array([4, 5, 1])
m2 = np.array([5, 1, 5])
print(np.dot(u, m1) / (np.linalg.norm(u) * np.linalg.norm(m1)))  # 0.7302967433402214
print(np.dot(u, m2) / (np.linalg.norm(u) * np.linalg.norm(m2)))  # 0.9704311900788593
#dot函数计算两个向量的点积，linalg.norm函数计算向量的模，两个向量的点积除以两个向量的模的乘积即为两个向量的夹角余弦值

##向量的叉积
print(np.cross(u, m1))  # [-14   7  21]
print(np.cross(m1, u))  # [ 14  -7 -21]

##矩阵
m1 = np.matrix('1 2 3; 4 5 6')
m1
m2 = np.asmatrix(np.array([[1, 1], [2, 2], [3, 3]]))
m2
m1 * m2

##线性代数
m3 = np.array([[1., 2.], [3., 4.]])
m4 = np.linalg.inv(m3)
m4
np.around(m3 @ m4)

###计算行列式
m5 = np.array([[1, 3, 5], [2, 4, 6], [4, 7, 9]])
np.linalg.det(m5)

###计算矩阵的秩
np.linalg.matrix_rank(m5)

###求解线性方程组
A = np.array([[1, 2, 1], [3, 7, 2], [2, 2, 1]])
b = np.array([8, 23, 9]).reshape(-1, 1)
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(np.hstack((A, b))))

np.linalg.solve(A, b)

np.linalg.inv(A) @ b

#多项式
p1 = np.poly1d([3, 2, 1])
p2 = np.poly1d([1, 2, 3])
print(p1)
print(p2)

##获取多项式的系数
print(p1.coefficients)
print(p2.coeffs)
##多项式的加减乘除
print(p1 + p2)
print(p1 * p2)
##带入值求解
print(p1(3))
print(p2(3))
##求导和不定积分
print(p1.deriv())
print(p1.integ())
##多项式的根
p3 = np.poly1d([1, 3, 2])
print(p3.roots)

from numpy.polynomial import Polynomial

p3 = Polynomial((2, 3, 1))
print(p3)           # 输出多项式
print(p3(3))        # 令x=3，计算多项式的值
print(p3.roots())   # 计算多项式的根
print(p3.degree())  # 获得多项式的次数
print(p3.deriv())   # 求导
print(p3.integ())   # 求不定积分

#最小二乘解
x = np.array([
    25000, 15850, 15500, 20500, 22000, 20010, 26050, 12500, 18500, 27300,
    15000,  8300, 23320,  5250,  5800,  9100,  4800, 16000, 28500, 32000,
    31300, 10800,  6750,  6020, 13300, 30020,  3200, 17300,  8835,  3500
])
y = np.array([
    2599, 1400, 1120, 2560, 1900, 1200, 2320,  800, 1650, 2200,
    980,  580, 1885,  600,  400,  800,  420, 1380, 1980, 3999,
    3800,  725,  520,  420, 1200, 4020,  350, 1500,  560,  500
])
import matplotlib.pyplot as plt

plt.figure(dpi=120)
plt.scatter(x, y, color='blue')
plt.show()

np.corrcoef(x, y)#计算相关系数

from numpy.polynomial import Polynomial

Polynomial.fit(x, y, deg=1).convert().coef

import matplotlib.pyplot as plt

plt.scatter(x, y, color='blue')
plt.scatter(x, 0.110333716 * x - 294.883437, color='red')
plt.plot(x, 0.110333716 * x - 294.883437, color='darkcyan')
plt.show()
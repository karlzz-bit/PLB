# NumPy - 数值计算库

## 简介
NumPy（Numerical Python）是 Python 语言的一个核心库，主要用于科学计算和数据处理。它提供了支持多维数组对象（`ndarray`）、各种数学函数、线性代数、随机数生成等功能。

NumPy 以高效的 C 语言实现，并针对数组运算进行了优化，因此比 Python 自带的列表操作要快得多。

## 安装
可以使用 `pip` 进行安装：

```sh
pip install numpy
```

## 主要特性
- **`ndarray` 多维数组对象**：高效存储和操作大规模数据。
- **广播机制**：支持不同形状数组的运算。
- **常用数学函数**：包括基本数学、线性代数、统计、傅里叶变换等。
- **索引和切片**：灵活访问数组中的数据。
- **随机数生成**：提供 `numpy.random` 模块进行随机数操作。


# NumPy 简介

NumPy（Numerical Python）是 Python 中用于科学计算的核心库，专注于高效处理大规模数组和矩阵运算。它不仅提供了一个强大的多维数组对象，还包含了丰富的数学函数和工具，可以让数值计算变得更加高效和简单。

## 主要功能

- **多维数组（ndarray）**  
  提供了高效的多维数组对象，支持快速、简便的数组操作和计算。

- **广播机制**  
  允许不同形状的数组进行运算，自动扩展较小数组，使得运算更加灵活。

- **数学函数库**  
  包含了丰富的数学、统计、傅里叶变换、线性代数等函数，能够处理从基础到复杂的数学运算。

- **线性代数**  
  提供矩阵运算、求逆、特征值与特征向量、行列式等常用的线性代数操作，适用于工程和科研领域。

- **随机数生成**  
  内置了强大的随机数生成模块，可以用于统计模拟、数据采样和机器学习等领域。

- **索引和切片**  
  支持灵活的索引和切片操作，使得对大规模数据的抽取和处理变得方便快捷。

## 应用领域

- **科学计算和工程**  
  在物理、化学、生物等自然科学领域中，用于处理实验数据和进行数值仿真。

- **数据分析和统计**  
  与其他数据分析库（如 pandas、scipy）结合，提供数据处理、清洗和统计分析功能。

- **机器学习和深度学习**  
  作为许多机器学习框架（例如 TensorFlow、PyTorch）的基础组件，加速大规模数据运算。

- **金融分析**  
  用于风险管理、时间序列分析和量化交易中的数值计算。


NumPy 凭借其高效的运算能力和丰富的功能，已成为科学计算和数据处理领域不可或缺的重要工具。
## 基本使用

### 导入 NumPy

```python
import numpy as np
```

### 创建数组

```python
# 从列表创建数组
arr = np.array([1, 2, 3, 4])
print(arr)  # 输出: [1 2 3 4]

# 创建多维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
```

### 数组属性

```python
print(arr.shape)  # 数组形状
print(arr.ndim)   # 数组维度
print(arr.size)   # 元素总数
print(arr.dtype)  # 数据类型
```

### 常见数组创建方法

```python
np.zeros((3, 3))       # 3x3 全 0 数组
np.ones((2, 2))        # 2x2 全 1 数组
np.eye(4)              # 4x4 单位矩阵
np.arange(0, 10, 2)    # 生成 0, 2, 4, 6, 8
np.linspace(0, 1, 5)   # 生成 0 到 1 之间的 5 个等间隔数
```

### 数组运算

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # 数组相加
print(arr1 * arr2)  # 逐元素相乘
print(arr1 ** 2)    # 平方运算
```

### 矩阵运算

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # 矩阵乘法
print(A @ B)         # 另一种矩阵乘法写法
```

### 索引和切片

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 1])   # 访问第一行第二列
print(arr[:, 1])   # 访问所有行的第二列
print(arr[1:, :2]) # 访问第二行及之后的前两列
```

### 统计函数

```python
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())    # 均值
print(arr.sum())     # 总和
print(arr.min())     # 最小值
print(arr.max())     # 最大值
print(arr.std())     # 标准差
```

### 随机数生成

```python
np.random.seed(42)               # 设置随机种子，确保可复现
print(np.random.rand(3, 3))       # 生成 3x3 0~1 之间的随机数
print(np.random.randint(0, 10, (2, 2)))  # 生成 2x2 的 0~9 之间的随机整数
```

## 进阶功能

### 广播机制（Broadcasting）

```python
A = np.array([[1], [2], [3]])  # 3x1 矩阵
B = np.array([4, 5, 6])        # 1x3 矩阵
print(A + B)  # 通过广播机制扩展维度后相加
```

### 形状变换

```python
arr = np.arange(6).reshape(2, 3)  # 变成 2x3 矩阵
print(arr)
print(arr.T)  # 转置
```

### 线性代数

```python
A = np.array([[3, 1], [1, 2]])
print(np.linalg.inv(A))  # 矩阵求逆
print(np.linalg.det(A))  # 矩阵行列式
print(np.linalg.eig(A))  # 特征值和特征向量
```

## 参考资料
- 官方文档: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
- GitHub: [https://github.com/numpy/numpy](https://github.com/numpy/numpy)

## 结论
NumPy 是 Python 进行数值计算的核心库，提供高效的数组操作和数学计算能力，广泛用于科学计算、数据分析和机器学习领域。
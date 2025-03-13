# 这是一个注释
import os
print(os.getcwd())  # 打印当前工作目录

import math
print(math.sqrt(16))

print("Hello, Python!")

#Python中的变量


#整型
#十进制输出
print(0b100)  # 二进制整数
print(type(0b100))  # 输出结果为<class 'int'>
print(0o100)  # 八进制整数
print(type(0o100))  # 输出结果为<class 'int'>
print(100)    # 十进制整数
print(type(100))    # 输出结果为<class 'int'>
print(0x100)  # 十六进制整数
print(type(0x100))  # 输出结果为<class 'int'>
#二进制输出
print(bin(100))  # 输出结果为0b1100100
#八进制输出
print(oct(100))  # 输出结果为0o144
#十六进制输出
print(hex(100))  # 输出结果为0x64

#浮点型
print(123.456)    # 数学写法
print(type(123.456))    # 输出结果为<class 'float'>
print(1.23456e2)  # 科学计数法
print(type(1.23456e2))  # 输出结果为<class 'float'>

#字符串型
print("Hello, Python!")  # 双引号字符串
print(type("Hello, Python!"))  # 输出结果为<class 'str'>

#布尔型
print(True)  # 输出结果为True
print(type(True))  # 输出结果为<class 'bool'>

#复数型
print(1 + 2j)  # 输出结果为(1+2j)
print(type(1 + 2j))  # 输出结果为<class 'complex'>


#数据类型转换
d=True
a=9+d         # 整型和布尔型相加
print(a)      # 输出结果为10 
print(int(False))  # 输出结果为0
print(int(True))   # 输出结果为1
print(float(False)) # 输出结果为0.0
print(float(True)) # 输出结果为1.0

# 运算符
sum_result = 5 + 3
diff_result = 5 - 3
prod_result = 5 * 3
quot_result = 5 / 2
floor_div_result = 5 // 2
mod_result = 5 % 2
exp_result = 5 ** 2
print(f"加法: {sum_result}, 减法: {diff_result}, 乘法: {prod_result}, 除法: {quot_result}, 地板除: {floor_div_result}, 取模: {mod_result}, 幂: {exp_result}")
# 比较运算符
print(5 > 3)   # True
print(5 < 3)   # False
print(5 >= 3)  # True
print(5 <= 3)  # False
print(5 == 3)  # False
print(5 != 3)  # True
# 逻辑运算符
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
# 位运算符
print(5 & 3)  # 按位与: 1
print(5 | 3)  # 按位或: 7
print(5 ^ 3)  # 按位异或: 6
print(~5)     # 按位取反: -6
print(5 << 1) # 左移: 10
print(5 >> 1) # 右移: 2
# 赋值运算符
x = 5
x += 3
print(x)  # 8
x -= 2
print(x)  # 6
x *= 2
print(x)  # 12
x /= 3
print(x)  # 4.0
x %= 3
print(x)  # 1.0
x //= 2
print(x)  # 0.0
x **= 3
print(x)  # 0.0
# 身份运算符
y = [1, 2, 3]
z = y
print(y is z)  # True
print(y is not z)  # False
# 成员运算符
print(1 in y)  # True
print(4 not in y)  # True
# 运算符优先级（从高到低）
# 1. 指数运算符: **
# 2. 按位取反: ~
# 3. 乘法、除法、取模、地板除: *, /, %, //
# 4. 加法、减法: +, -
# 5. 按位移位运算符: <<, >>
# 6. 按位与: &
# 7. 按位异或: ^
# 8. 按位或: |
# 9. 比较运算符: ==, !=, >, >=, <, <=, is, is not, in, not in
# 10. 逻辑运算符: not, and, or

#海象运算符
print(x := 5)  # 输出结果为5

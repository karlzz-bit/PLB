# 这是一个注释
import os
print(os.getcwd())  # 打印当前工作目录

import math
print(math.sqrt(16))

print("Hello, Python!")

#Python中的数据类型
a = 10        # 整型变量
print(type(a))
b = 3.14e2    # 浮点型变量
print(type(b))
c = 1 + 2j    # 复数变量
print(type(c))
d=True        # 布尔型变量
print(type(d))
e = "Hello"   # 字符串变量
print(type(e))
#数据类型转换
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

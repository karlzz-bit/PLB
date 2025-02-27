# 这是一个注释
import os
print(os.getcwd())  # 打印当前工作目录

import math
print(math.sqrt(16))


print("Hello, Python!")
a = 10        # 整型变量
b = 3.14      # 浮点型变量
c = "Hello"   # 字符串变量
num_int = 100
num_float = 3.14
num_complex = 2 + 3j
greeting = "Hello, Python"
#list
fruits = ["apple", "banana", "cherry"]
#tuple
point = (10, 20)
#dict
person = {"name": "Alice", "age": 25}
person["name"]="hhe"
print(person)
#set
unique_nums = {1, 2, 3, 2}
print(unique_nums)
#控制流
    #条件控制
if a > 5:
    print("a 大于 5")
elif a == 5:
    print("a 等于 5")
else:
    print("a 小于 5")
    #循环控制
for i in range(5):
    print(i)
count = 0
while count < 5:
    print(count)
    count += 1
#函数
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
square = lambda x: x * x
print(square(5))
# 文件路径
file_path = "example.txt"

# 检查文件是否存在
if not os.path.exists(file_path):
    # 如果文件不存在，创建并写入一些内容
    with open(file_path, "w") as file:
        file.write("Hello, this is a new file!\n")
        file.write("This file was created because it didn't exist.\n")
    print(f"文件 {file_path} 已创建并写入内容。")

# 读取文件内容
with open(file_path, "r") as file:
    content = file.read()
    print(content)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("不能除以0")
finally:
    print("执行结束")

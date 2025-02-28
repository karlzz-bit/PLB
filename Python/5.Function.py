# Function 函数

# 定义一个简单的函数
def greet(name):
    """这个函数用于问候某人"""
    print(f"Hello, {name}!")

# 调用函数：使用位置参数调用函数
greet("Alice")

# 使用关键字参数调用函数
def greet_with_message(name, message):
    """这个函数用于问候某人并传递一条消息"""
    print(f"Hello, {name}! {message}")

greet_with_message(name="Bob", message="How are you today?")

# 参数的默认值
def greet_with_default_message(name, message="Have a great day!"):
    """这个函数用于问候某人并传递一条默认消息"""
    print(f"Hello, {name}! {message}")

greet_with_default_message("Charlie")
greet_with_default_message("David", "Good luck with your project!")

# 可变参数：基于元组的可变参数
def greet_multiple_people(*names):
    """这个函数用于问候多个人"""
    for name in names:
        print(f"Hello, {name}!")

greet_multiple_people("Eve", "Frank", "Grace")

# 可变参数：基于字典的可变参数
def greet_with_details(**details):
    """这个函数用于问候某人并提供详细信息"""
    for key, value in details.items():
        print(f"{key}: {value}")

greet_with_details(name="Hank", age=30, location="New York")

# 函数中变量的作用域
def scope_example():
    """这个函数展示了变量的作用域"""
    local_var = "I am local"
    print(local_var)

scope_example()
# print(local_var)  # 这行代码会报错，因为local_var是局部变量

# 函数类型：理解函数类型，过滤函数filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 映射函数map()
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Lambda函数
# 一个简单的lambda函数用于计算两个数的和
add = lambda x, y: x + y
print(add(3, 5))
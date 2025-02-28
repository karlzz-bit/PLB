# String 字符串

from collections import Counter

# 普通字符串
normal_str = "Hello, World!"
# 打印普通字符串
print(f"普通字符串: {normal_str}")

# 原始字符串
raw_str = r"C:\Users\Name\Documents"
# 打印原始字符串
print(f"原始字符串: {raw_str}")

# 长字符串
long_str = """This is a long string
that spans multiple lines."""
# 打印长字符串
print(f"长字符串: {long_str}")

# 字符串与数字的相互转换

# 将字符串转换为数字
num_str = "123"
num = int(num_str)  # 转换为整数
# 打印转换后的整数
print(f"字符串转换为整数: {num}")
float_num = float(num_str)  # 转换为浮点数
# 打印转换后的浮点数
print(f"字符串转换为浮点数: {float_num}")

# 将数字转换为字符串
num = 123
num_str = str(num)  # 转换为字符串
# 打印转换后的字符串
print(f"数字转换为字符串: {num_str}")

# 格式化字符串

# 使用占位符
name = "Alice"
age = 30
formatted_str = "My name is %s and I am %d years old." % (name, age)
# 打印使用占位符格式化的字符串
print(f"使用占位符格式化字符串: {formatted_str}")

# 使用format方法
formatted_str = "My name is {} and I am {} years old.".format(name, age)
# 打印使用format方法格式化的字符串
print(f"使用format方法格式化字符串: {formatted_str}")

# 使用f-string (Python 3.6+)
formatted_str = f"My name is {name} and I am {age} years old."
# 打印使用f-string格式化的字符串
print(f"使用f-string格式化字符串: {formatted_str}")

# 操作字符串

# 字符串查找
text = "Hello, World!"
index = text.find("World")  # 返回子字符串的起始索引，找不到返回-1
# 打印字符串查找结果
print(f"字符串查找 'World' 的索引: {index}")

# 字符串替换
new_text = text.replace("World", "Python")  # 替换子字符串
# 打印字符串替换后的结果
print(f"字符串替换后的结果: {new_text}")

# 字符串分割
split_text = text.split(", ")  # 按指定分隔符分割字符串，返回列表
# 打印字符串分割后的结果
print(f"字符串分割后的结果: {split_text}")

# 统计文章中单词出现的频率

article = "This is a sample article. This article is just a sample."

# 将文章分割为单词列表
words = article.split()
# 打印文章分割为单词列表的结果
print(f"文章分割为单词列表: {words}")

# 统计单词出现的频率
word_count = Counter(words)
# 打印单词出现的频率
print(f"单词出现的频率: {word_count}")
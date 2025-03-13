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

# 字符串 (String)
s1 = 'hello, world!'
s2 = "你好，世界！❤️"
s3 = '''hello,
wonderful
world!'''
print(s1)
print(s2)
print(s3)
#转义字符
s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)
#原始字符串
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)
#\t,\r,\n转义字符
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1)
print(s2)
#字符串的运算
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!
#比较运算
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
#成员运算
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)      # True
print('wo' not in s2)  # False
print(s2 in s1)        # False

#字符串的方法
s1 = 'hello, world!'

# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE
#查找字符串
s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
# print(s.index('or', 9))  # ValueError: substring not found
s = 'hello world!'
print(s.find('o'))       # 4
print(s.rfind('o'))      # 7
print(s.rindex('o'))     # 7
# print(s.rindex('o', 8))  # ValueError: substring not found
#性质判断
s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False
print(s2.isalpha())  # False
print(s2.isalnum())  # True
#格式化
s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))
a = 321
b = 123
print(f'{a} * {b} = {a * b}')
#修剪
s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界
#替换
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world
#拆分与合并
s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']
#编码与解码
a = 'zz'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)                  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))    # 骆昊
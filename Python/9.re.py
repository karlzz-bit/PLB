import re

#基本匹配
pattern = r'hello'
text = 'hello world'

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

#搜索
pattern = r'world'
text = 'hello world'

search = re.search(pattern, text)
if search:
    print("Search found:", search.group())
else:
    print("No match")

#查找所有匹配项
pattern = r'\d+'
text = 'There are 123 apples and 456 oranges.'

matches = re.findall(pattern, text)
print("All matches:", matches)

#替换
pattern = r'apples'
replacement = 'bananas'
text = 'I like apples.'

new_text = re.sub(pattern, replacement, text)
print("Replaced text:", new_text)

#分割
pattern = r'\s+'
text = 'Split this text by spaces.'

split_text = re.split(pattern, text)
print("Split text:", split_text)

#编译正则表达式
pattern = re.compile(r'\d+')
text = 'There are 123 apples and 456 oranges.'

matches = pattern.findall(text)
print("All matches:", matches)

"""
常用正则表达式符号
- `.`: 匹配任意字符（除换行符）
- `^`: 匹配字符串的开头
- `$`: 匹配字符串的结尾
- `*`: 匹配前面的字符零次或多次
- `+`: 匹配前面的字符一次或多次
- `?`: 匹配前面的字符零次或一次
- `{n}`: 匹配前面的字符恰好n次
- `{n,}`: 匹配前面的字符至少n次
- `{n,m}`: 匹配前面的字符至少n次，至多m次
- `[]`: 匹配字符集中的任意一个字符
- `|`: 匹配左右任意一个表达式
- `\`: 转义字符
"""
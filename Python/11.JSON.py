import json
# JSON (JavaScript对象表示法) 是一种轻量级的数据交换格式。
# 它易于人类阅读和编写，也易于机器解析和生成。
# JSON基于两种结构：
# 1. 名称/值对的集合（通常实现为对象、记录、结构、字典、哈希表、键控列表或关联数组）。
# 2. 值的有序列表（通常实现为数组、向量、列表或序列）。

# JSON数据示例
json_data = '''
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "children": []
}
'''

# 解析JSON数据
data = json.loads(json_data)

# 访问数据
print(data['name'])  # 输出: John
print(data['age'])   # 输出: 30

# 将Python对象转换为JSON字符串
python_data = {
    "name": "Jane",
    "age": 25,
    "city": "Los Angeles",
    "hasChildren": True,
    "children": ["Alice", "Bob"]
}


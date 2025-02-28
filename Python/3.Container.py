# Python Container

# 序列 (Sequence)
sequence = range(1, 10)
print("\n序列:", list(sequence))
print("序列的第一个元素:", sequence[0])
print("序列的长度:", len(sequence))

# 列表 (List)
fruits = ["apple", "banana", "cherry"]
print("\n列表:", fruits)
fruits.append("orange")
print("添加元素后的列表:", fruits)
print("列表的第一个元素:", fruits[0])
print("列表的长度:", len(fruits))
fruits.remove("banana")
print("移除元素后的列表:", fruits)

# 元组 (Tuple)
vegetables = ("carrot", "potato", "cucumber")
print("\n元组:", vegetables)
print("元组的第一个元素:", vegetables[0])
print("元组的长度:", len(vegetables))

# 集合 (Set)
unique_numbers = {1, 2, 3, 4, 5}
print("\n集合:", unique_numbers)
unique_numbers.add(6)
print("添加元素后的集合:", unique_numbers)
unique_numbers.remove(3)
print("移除元素后的集合:", unique_numbers)
print("集合的长度:", len(unique_numbers))

# 字典 (Dictionary)
student = {"name": "John", "age": 25, "courses": ["Math", "Science"]}
print("\n字典:", student)
print("学生的名字:", student["name"])
student["age"] = 26
print("更新年龄后的字典:", student)
student["courses"].append("History")
print("更新课程后的字典:", student)
print("字典的所有键:", student.keys())
print("字典的所有值:", student.values())
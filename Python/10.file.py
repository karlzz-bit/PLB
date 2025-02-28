
# 打开文件进行写操作，如果文件不存在则会创建
with open('example.txt', 'w') as file:
    # 写入内容到文件
    file.write('Hello, World!\n')
    file.write('This is a test file.\n')

# 打开文件进行追加操作
with open('example.txt', 'a') as file:
    # 追加内容到文件末尾
    file.write('Appending a new line.\n')

# 打开文件进行读操作
with open('example.txt', 'r') as file:
    # 读取文件的所有内容
    content = file.read()
    print('File Content:')
    print(content)

# 打开文件进行逐行读取
with open('example.txt', 'r') as file:
    print('Reading file line by line:')
    for line in file:
        print(line.strip())  # 使用strip()去除每行末尾的换行符
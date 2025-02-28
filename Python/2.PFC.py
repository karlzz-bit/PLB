# Python program flow control
#程序流程控制
# 条件语句
def check_number(num):
    if num > 0:
        print("这是一个正数")
    elif num == 0:
        print("这是零")
    else:
        print("这是一个负数")

# 循环语句
def print_numbers(n):
    for i in range(n):
        print(i)

# while 循环
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("倒计时结束")

# break 和 continue
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"找到第一个偶数: {num}")
            break
    else:
        print("没有找到偶数")

def skip_odd_numbers(numbers):
    for num in numbers:
        if num % 2 != 0:
            continue
        print(f"偶数: {num}")

# 函数调用示例
if __name__ == "__main__":
    check_number(10)
    check_number(0)
    check_number(-5)

    print_numbers(5)

    countdown(5)

    find_first_even([1, 3, 5, 7, 8, 9])
    skip_odd_numbers([1, 2, 3, 4, 5, 6])
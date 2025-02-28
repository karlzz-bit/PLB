# 除零异常
i=input("请输入一个数字：")
n=8888
result = n / int(i)
print(result)
print("{0}除以{1}的结果是{2}".format(n,i,result))#如果输入0，会报错，因为除数不能为0。

#try-except语句
i=input("请输入一个数字：")
n=8888
try:
    result = n / int(i)
    print(result)
    print("{0}除以{1}的结果是{2}".format(n,i,result))
except ZeroDivisionError:
    print("除数不能为0！")
except ValueError:
    print("输入的值不是数字！")

#多重异常捕获
i=input("请输入一个数字：")
n=8888
try:
    result = n / int(i)
    print(result)
    print("{0}除以{1}的结果是{2}".format(n,i,result))
except (ZeroDivisionError,ValueError):
    print("输入的值不合法！")

#try-except语句嵌套
i=input("请输入一个数字：")
n=8888
try:
    i2=int(i)
    try:
        result = n / i2
        print(result)
        print("{0}除以{1}的结果是{2}".format(n,i,result))
    except ZeroDivisionError as e:
        print("除数不能为0！")
except ValueError as e:
    print("输入的值不是数字！")


# finally 
i=input("请输入一个数字：")
n=8888
try:
    result = n / int(i)
    print(result)
    print("{0}除以{1}的结果是{2}".format(n,i,result))
except ZeroDivisionError as e:
    print("除数不能为{}！".format(e))
except ValueError as e:
    print("输入的值不是数字！异常：{}".format(e))
finally:
    print("程序执行完毕！")


# 自定义异常类示例
class CustomError(Exception):
    def __init__(self,message):
        super().__init__(message)
        
i=input("请输入一个数字：")
n=8888
try:
    result = n / int(i)
    print(result)
    print("{0}除以{1}的结果是{2}".format(n,i,result))
except ZeroDivisionError as e:
    raise CustomError("除数不能为0！")
except ValueError as e:
    raise CustomError("输入的值不是数字！异常：{}".format(e))
finally:
    print("程序执行完毕！")
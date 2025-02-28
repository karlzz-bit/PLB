# 面向对象编程

#面向对象
"""
面向对象编程(Object-Oriented Programming,简称OOP)是一种编程范式,它使用“对象”来设计应用程序和计算机程序。
对象是类的实例,类是定义对象属性和行为的蓝图。Python是一种支持面向对象编程的语言。

以下是Python中面向对象编程的一些基本概念:

1. 类(Class)：类是创建对象的模板。它定义了一组属性和方法，这些属性和方法是对象所共有的。
2. 对象(Object)：对象是类的实例。每个对象都有属于自己的属性和方法。
3. 属性(Attributes)：属性是对象的状态或数据。它们在类中定义，并在对象实例化时赋值。
4. 方法(Methods)：方法是定义在类中的函数，用于描述对象的行为。
5. 继承(Inheritance)：继承是一个类（子类）从另一个类（父类）继承属性和方法的机制。它促进代码重用和层次化。
6. 封装(Encapsulation)：封装是将数据和方法捆绑在一起，并隐藏对象的内部状态以防止外部干扰的机制。
7. 多态(Polymorphism)：多态是指不同类的对象可以通过相同的接口调用，从而实现不同的行为。
"""
#定义类
class Car(object):
    #类体
    pass    #`pass` 语句在 Python 中是一个占位符，用于在语法上需要一个语句但实际上不需要执行任何代码的地方。

#创建对象
car=Car()   #创建一个名为`car`的`Car`类的对象。
#这行代码调用了 Car类的构造函数 Car()，创建了一个 Car类的实例(对象）。
#car这是一个变量,用于引用新创建的Car对象。


#类的成员
"""
类的成员是类中定义的变量和方法，它们描述了类的属性和行为。类的成员主要包括以下几种：

1. 实例变量：每个对象独有的属性，在构造方法中定义，使用 `self` 关键字引用。
2. 构造方法：在创建对象时自动调用，用于初始化对象的属性，通常是 `__init__` 方法。
3. 实例方法：定义在类中的函数，用于描述对象的行为，第一个参数通常是 `self`，表示对象本身。
4. 类变量：类的所有实例共享的属性，定义在类体中，通常在方法外部。
5. 类方法：使用 `@classmethod` 装饰器定义的方法，第一个参数是类本身，通常是 `cls`。
6. 静态方法：使用 `@staticmethod` 装饰器定义的方法，不需要传递类或实例的引用。

"""
#实例变量
class Dog:
    def __init__(self, name, age,sex="雌性"):  #这是构造方法的定义。`__init__` 是一个特殊的方法名，在创建类的实例时自动调用。
        self.name = name            #这行代码将传递给构造函数的 name 参数赋值给实例的 name 属性。
        self.age = age              #这行代码将传递给构造函数的 age 参数赋值给实例的 age 属性。
        self.sex=sex
d=Dog(name="Buddy",age=2)           #创建一个名为`d`的`Dog`类的对象。
print(f"{d.name} is {d.age} years old.")  #输出结果为：Buddy is 2 years old.
#构造方法
#构造方法是一个特殊的方法，用于在创建类的实例时初始化对象的属性。构造方法的第一个参数通常是 `self`，表示对象本身。
d1=Dog(name="Buddy",age=2)  #创建一个名为`d1`的`Dog`类的对象。
d2=Dog("d2",3,"雄性")    #创建一个名为`d2`的`Dog`类的对象。
d3=Dog(sex="雌性",name="d3",age=4)    #创建一个名为`d3`的`Dog`类的对象。
#实例方法
class Dog2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):  #这是一个实例方法的定义。第一个参数通常是 `self`，表示对象本身。
        return f"{self.name} is running."
    def speak(self,sound):
        print(f"{self.name} says {sound}")
dog1=Dog2(name="Buddy",age=2)  #创建一个名为`dog1`的`Dog2`类的对象。
print(dog1.run())  #输出结果为：Buddy is running.
dog1.speak("Woof!")  #输出结果为：Buddy says Woof!
#类变量
class Account:
    interest_rate = 0.05  #这是一个类变量的定义。类变量在类的所有实例之间共享。
    def __init__(self, owner,amount):
        self.owner = owner
        self.amount = amount
account=Account(owner="Alice",amount=1000)  #创建一个名为`account`的`Account`类的对象。
print(f"{account.owner} has an interest rate of {account.interest_rate}.")  #输出结果为：Alice has an interest rate of 0.05.
print(f"{account.owner} has an amount of {Account.amount}.")  #输出结果为：Alice has an amount of 1000.
#类方法
"""
类方法是定义在类中的方法，它的第一个参数是类本身，而不是实例对象。
类方法使用 `@classmethod` 装饰器来定义。类方法可以访问和修改类状态，即它们可以访问类变量和调用其他类方法，但不能直接访问实例变量。
"""
class Account2:
    interest_rate = 0.05
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount
    @classmethod
    def interest_by(cls, amt):  #这是一个类方法的定义。使用 `@classmethod` 装饰器定义。
        return cls.interest_rate * amt
interest=Account2.interest_by(1000)  #调用类方法
print(f"Interest on $1000 is ${interest}.")  #输出结果为：Interest on $1000 is $50.0.


#封装性
"""
封装性(Encapsulation)是面向对象编程(OOP)中的一个核心概念，它指的是将数据（属性）和操作数据的行为（方法）捆绑在一起，形成一个独立的单元（类）。
封装通过隐藏对象的内部实现细节,只暴露必要的接口来保护数据的安全性和完整性。
"""
#私有变量和私有方法
class Account_P:
    __interest_rate = 0.05  #这是一个私有类变量的定义。私有变量以两个下划线开头。
    def __init__(self, owner, amount):
        self.owner = owner
        self.__amount = amount #这是一个私有实例变量的定义。私有变量以两个下划线开头。
    def __get_info(self):  #这是一个私有方法的定义。私有方法以两个下划线开头。
        return f"{self.owner} has ${self.__amount}."
    def desc(self):
        print("{0}金额:{1}利率:{3}".format(self.owner,self.__amount,Account_P.__interest_rate))  #这是一个实例方法的定义。
account23=Account_P(owner="Alice",amount=1000)  #创建一个名为`account23`的`Account_P`类的对象。
account23.desc()  #输出结果为：Alice金额:1000利率:0.05
print(account23.owner)  #输出结果为：Alice
print(account23.__amount)  #这行代码会报错，因为`__amount`是一个私有变量。
print(account23.__interest_rate)  #这行代码会报错，因为`__interest_rate`是一个私有变量。
print(account23.__get_info())  #这行代码会报错，因为`__get_info()`是一个私有方法。
#使用属性
class Dog_A:
    def __init__(self,name,age,sex="雌性"):
        self.name=name #这是一个实例变量的定义。
        self.__age=age #这是一个私有实例变量的定义。
    def run(self):
        return f"{self.name} is running."
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
dog546=Dog_A(name="Buddy",age=2)  #创建一个名为`dog546`的`Dog_A`类的对象。
print(dog546.get_age())  #输出结果为：2
print(dog546.set_age(3))  #输出结果为：None
print(dog546.__age)  #这行代码会报错，因为`__age`是一个私有变量。


#继承性
class Animal:
    def __init__(self, name):
        self.name = name
    def show_info(self):
        return f"I am {self.name}."
    def move(self):
        return "I can move."
class Cat(Animal):  #这是一个子类的定义。子类继承了父类的属性和方法。
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
cat=Cat(name="Kitty",age=2)  #创建一个名为`cat`的`Cat`类的对象。
print(cat.move()) #输出结果为：I can move.
print(cat.show_info())  #输出结果为：I am Kitty.
print(cat.age)  #输出结果为：2
#多重继承
class Horse:
    def __init__(self,name):
        self.name = "Horse"
    def show_info(self):
        return f"I am {self.name}."
    def run(self):
        return "Horse run."
class Donkey:
    def __init__(self,name):
        self.name = name
        def show_info(self):
            return f"I am {self.name}."
        def run(self):
            return "Donkey run."
        def roll(self):
            return "Donkey roll."
class Mule(Horse,Donkey):  #这是一个多重继承的子类的定义。子类继承了多个父类的属性和方法。
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
m=Mule(name="Mule",age=3)  #创建一个名为`m`的`Mule`类的对象。
print(m.run())  #输出结果为：Horse run.
print(m.roll())  #输出结果为：Donkey roll.
print(m.show_info())  #输出结果为：I am Mule.
#方法重写
class Mule(Horse,Donkey):  #这是一个多重继承的子类的定义。子类继承了多个父类的属性和方法。
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show_info(self):
        return super().show_info()+"I am a mule."
m1=Mule(name="Mule",age=3)
print(m1.show_info())  #输出结果为：I am Mule.I am a mule.

#多态
"""
多态是面向对象编程中的一个核心概念，它指的是一个对象可以表现出多种形态的行为。
简单来说，多态允许我们通过一个统一的接口或父类引用来操作不同类型的对象，而程序会在运行时根据对象的实际类型来执行相应的方法。
"""
#继承和多态
class Animals:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "I am an animal."
class Dogs(Animals):
    def speak(self):
        return "I am a dog."
class Cats(Animals):
    def speak(self):
        return "I am a cat."
an1=Animals("Animal")
an2=Dogs("Dog")
an3=Cats("Cat")
print(an1.speak())  #输出结果为：I am an animal.
print(an2.speak())  #输出结果为：I am a dog.
print(an3.speak())  #输出结果为：I am a cat.
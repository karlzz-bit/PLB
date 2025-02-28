#include <iostream>
#include <string>

// 基类：动物
class Animal {
public:
    // 构造函数
    Animal(const std::string& name) : name(name) {}

    // 虚函数：发出声音
    virtual void makeSound() const {
        std::cout << name << " makes a sound." << std::endl;
    }

    // 获取动物的名字
    std::string getName() const {
        return name;
    }

protected:
    std::string name; // 动物的名字
};

// 派生类：狗
class Dog : public Animal {
public:
    // 构造函数
    Dog(const std::string& name) : Animal(name) {}

    // 重写基类的虚函数
    void makeSound() const override {
        std::cout << name << " barks." << std::endl;
    }
};

// 派生类：猫
class Cat : public Animal {
public:
    // 构造函数
    Cat(const std::string& name) : Animal(name) {}

    // 重写基类的虚函数
    void makeSound() const override {
        std::cout << name << " meows." << std::endl;
    }
};

int main() {
    // 创建动物对象
    Animal genericAnimal("Generic Animal");
    Dog dog("Buddy");
    Cat cat("Whiskers");

    // 调用发出声音的方法
    genericAnimal.makeSound();
    dog.makeSound();
    cat.makeSound();

    // 使用基类指针指向派生类对象
    Animal* animalPtr = &dog;
    animalPtr->makeSound(); // 调用的是Dog类的makeSound方法

    animalPtr = &cat;
    animalPtr->makeSound(); // 调用的是Cat类的makeSound方法

    return 0;
}
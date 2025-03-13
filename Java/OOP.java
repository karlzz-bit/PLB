class Star {
    public String name;
    public int age;
    public double height;
    public int weight;
    public void sayHello(String target) {
        System.out.println(name + " says: Hello, " + target + "!");
    }
    void sayGoodbye(String target) {
        System.out.println(name + " says: Goodbye, " + target + "!");
    }
    private void sayGoodnight(String target) {
        System.out.println(name + " says: Goodnight, " + target + "!");
    }
    void sayGoodnightPublic(String target) {
        sayGoodnight(target);
    }

}
public class OOP {
    public static void main(String[] args) {
        // 创建一个Star对象
        Star star = new Star();
        // 设置字段
        star.name = "张三";
        star.age = 25;
        star.height = 1.78;
        star.weight = 72;
        // 访问字段
        System.out.println(star.name);
        System.out.println(star.age);
        System.out.println(star.height);
        System.out.println(star.weight);
        // 调用方法
        star.sayHello("李四");
        star.sayGoodbye("王五");
        // star.sayGoodnight("赵六"); // 编译错误
        star.sayGoodnightPublic("赵六");
        System.out.println(star);
        
    }
}
//这是一个简单的Java程序
/*
 * 这是一个多行注释的例子
 * 这是一个简单的Java程序
 * 保存文件名为HelloJava.java
 */

import java.util.Scanner;

public class HelloJava {// 类名
    // 成员变量
    private int instanceVar;
    // 静态变量
    private static int staticVar;
    public void method(int paramVar) {
        // 局部变量
        int localVar = 10;
        
        // 使用变量
        instanceVar = localVar;
        staticVar = paramVar;
        
        System.out.println("成员变量: " + instanceVar);
        System.out.println("静态变量: " + staticVar);
        System.out.println("参数变量: " + paramVar);
        System.out.println("局部变量: " + localVar);
    }
    public static void main(String[] args) {//main方法
        System.out.println("Hello Java");
        int x=1;
        int y=x;
        System.out.println(x);
        x=x+y;
        System.out.println(x);
        printV();//展示变量范围
        HelloJava v = new HelloJava();
        v.method(10);//调用方法
        //输出
        System.out.print("A,");
        System.out.print("B,");
        System.out.print("C.");
        System.out.println();
        System.out.println("END");
        //格式化输出
        double d = 12900000;
        System.out.println(d); // 1.29E7
        double e = 3.1415926;
        System.out.printf("%.2f\n", e); // 显示两位小数3.14
        System.out.printf("%.4f\n", e); // 显示4位小数3.1416
        int n = 12345000;
        System.out.printf("n=%d, hex=%08x", n, n); // 注意，两个%占位符必须传入两个数
        System.out.println();
        //输入
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input your name: ");
        String name = scanner.nextLine();
        System.out.print("Input your age: ");
        int age = scanner.nextInt();
        System.out.printf("Hi, %s, you are %d\n", name, age);
        scanner.close();//
        
        
    }
    // 定义静态变量，所有方法都能访问
    static byte byteVar = 127; // 范围: -128 ~ 127
    static short shortVar = 32767; // 范围: -32,768 ~ 32,767
    static int intVar = 2_147_483_647; // 范围: -2^31 ~ 2^31-1
    static long longVar = 9_223_372_036_854_775_807L; // 范围: -2^63 ~ 2^63-1
    static float floatVar = 3.14F;
    static double doubleVar = 3.141592653589793;
    static char charVar = 'A';
    static char unicodeChar = '\u4F60'; // '你'
    static boolean boolVar = true;
    static String stringVar = "Hello, Java!";

    // 定义静态方法，所有方法都能访问
    public static void printV(){
        System.out.println("test");
        // 🌟 输出所有变量的值和取值范围
        System.out.println("===== 整数类型 =====");
        System.out.println("byte: " + byteVar + " (范围: " + Byte.MIN_VALUE + " ~ " + Byte.MAX_VALUE + ")");
        System.out.println("short: " + shortVar + " (范围: " + Short.MIN_VALUE + " ~ " + Short.MAX_VALUE + ")");
        System.out.println("int: " + intVar + " (范围: " + Integer.MIN_VALUE + " ~ " + Integer.MAX_VALUE + ")");
        System.out.println("long: " + longVar + " (范围: " + Long.MIN_VALUE + " ~ " + Long.MAX_VALUE + ")");

        System.out.println("\n===== 浮点数类型 =====");
        System.out.println("float: " + floatVar + " (范围: " + Float.MIN_VALUE + " ~ " + Float.MAX_VALUE + ")");
        System.out.println("double: " + doubleVar + " (范围: " + Double.MIN_VALUE + " ~ " + Double.MAX_VALUE + ")");

        System.out.println("\n===== 字符类型 =====");
        System.out.println("char: " + charVar + " (Unicode: " + (int) charVar + ")");
        System.out.println("Unicode char: " + unicodeChar + " (Unicode: " + (int) unicodeChar + ")");

        System.out.println("\n===== 布尔类型 =====");
        System.out.println("boolean: " + boolVar);

        System.out.println("\n===== 字符串类型 =====");
        System.out.println("String: " + stringVar);
    }
}
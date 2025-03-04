class Person {
    public String name;
    public int age;
}
class Book {
    public String name;
    public String author;
    public String isbn;
    public double price;
}
public class OOP {
    public static void println() {
        System.out.println("hello");
    }
    public static void main(String[] args) {
        Person ming = new Person();
        Book book = new Book();
        System.out.println(book.name); // null
        System.out.println(book.price); // 0.0
        System.out.println(ming.name); // null
        System.out.println(ming.age); // 0
        ming.name = "Xiao Ming";
        ming.age = -99; // age设置为负数
        println();
    }
}
public class PFC {
    public static void main(String[] args) {
        
        //条件判断
        int x = 70;
        if (x >= 90) {
            System.out.println("优秀");//当if语句块只有一行语句时,可以省略花括号{}
        }else if (x >= 60) {
            System.out.println("及格");
        }else if (x==59) {
            System.out.println("差一分");
        }else{
            System.out.println("不及格");
        }
        System.out.println("END");
        //switch
        int option = 1;
        switch (option) {
        case 1:
            System.out.println("Selected 1");
            break;
        case 2:
        case 3:
            System.out.println("Selected 2 or 3 ");
            break;
        default:
            System.out.println("Not selected");
            break;
        }
        String fruit = "orange";
        int opt = switch (fruit) {
            case "apple" -> 1;
            case "pear", "mango" -> 2;
            default -> {
                int code = fruit.hashCode();
                yield code; // switch语句返回值
            }
        };
        System.out.println("opt = " + opt);
        //循环
        int sum = 0; // 累加的和,初始化为0
        int n = 1;
        while (n <= 100) { // 循环条件是n <= 100
            sum = sum + n; // 把n累加到sum中
            n ++; // n自身加1
        }
        System.out.println(sum); // 5050、
        //do while
        int sum1 = 0;
        int n1 = 1;
        do {
            sum1 = sum1 + n1;
            n1 ++;
        } while (n1 <= 100);
        System.out.println(sum1);
        //for
        int sum2 = 0;
        for (int i=1; i<=100; i++) {
            sum2 = sum2 + i;
        }
        System.out.println(sum2);
        int[] ns = { 1, 4, 9, 16, 25 };
        for (int i=0; i<ns.length; i++) {
            System.out.println(ns[i]);
            i = i + 1;
        }
        //for each
        for (int i : ns) {
            System.out.println(i);
        }
        //break,continue
        int sum3 = 0;
        for (int i=1; ; i++) {
            sum3 = sum3 + i;
            if (i == 100) {
                break; // 通过break跳出循环
            }
        }
        System.out.println(sum3);
        for (int i=1; i<=10; i++) {
            System.out.println("i = " + i);
            for (int j=1; j<=10; j++) {
                System.out.println("j = " + j);
                if (j >= i) {
                    break;
                }
            }
            // break跳到这里
            System.out.println("breaked");
        }
        int sum0 = 0;
        for (int i=1; i<=10; i++) {
            System.out.println("begin i = " + i);
            if (i % 2 == 0) {
                continue; // continue语句会结束本次循环
            }
            sum0 = sum0 + i;
            System.out.println("end i = " + i);
        }
        System.out.println(sum0); // 25
    }
}

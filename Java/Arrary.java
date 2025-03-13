public class Arrary {
    public static void main(String[] args) {
        // 定义一个int数组变量
        int[] ns = { 1, 1, 2, 3, 5, 8 };
        // 求和
        int sum = 0;
        for (int i = 0; i < ns.length; i++) {
            sum = sum + ns[i];
        }
        System.out.println(sum); // 20
    }
    public static void twoDimensionalArrayExample() {
        // 定义一个二维int数组变量
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // 打印二维数组
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}

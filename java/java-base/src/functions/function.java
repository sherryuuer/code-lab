import java.util.Arrays;

public class function {
    public static void main(String[] args) {
        int[] array = new int[] { 9, 10, 0, 2, 87, 2 };
        sort(array);
        System.out.println(Arrays.toString(array));

        // 没有static字段的函数，需要创建类的实例，通过实例调用非静态的func方法
        function example = new function();
        int[] A = example.func(array);
        System.out.println(Arrays.toString(A));
    }

    // void为空无一物伽蓝道不能return，所以要改为return的type
    // 这是一个静态方法，所以主类中可以直接调用，如果没有static则需要实例化
    public static void sort(int[] A) {

        for (int i = 0; i < A.length - 1; i++) {
            for (int j = A.length - 1; j >= i + 1; j--) {
                if (A[j] < A[j - 1]) {
                    replacement(A, j);
                }
            }
        }
    }

    // replace function
    public static void replacement(int[] A, int j) {
        int w;
        w = A[j];
        A[j] = A[j - 1];
        A[j - 1] = w;
    }

    // 非静态方法
    public int[] func(int[] A) {
        int w;

        for (int i = 0; i < A.length - 1; i++) {
            for (int j = A.length - 1; j >= i + 1; j--) {
                if (A[j] < A[j - 1]) {
                    w = A[j];
                    A[j] = A[j - 1];
                    A[j - 1] = w;
                }
            }
        }

        return A;
    }
}

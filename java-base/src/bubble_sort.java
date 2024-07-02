import java.util.Arrays;

public class bubble_sort {
    public static void main(String[] args) {
        int[] A = new int[] { 9, 10, 0, 2, 87, 2 };
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

        System.out.println(Arrays.toString(A));
    }
}

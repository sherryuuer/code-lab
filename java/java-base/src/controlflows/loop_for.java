import java.util.Arrays;

public class loop_for {
    public static void main(String[] args) {
        int[] array = new int[] { 1, 2, 3, 4, 5 };
        int right;
        int tmp;

        for (int left = 0; left < array.length / 2; left = left + 1) { // 也可以是++
            right = array.length - left - 1;
            tmp = array[right];
            array[right] = array[left];
            array[left] = tmp;
        }

        System.out.println(Arrays.toString(array));

        for (int idx = 0; idx < array.length; idx++) {
            System.out.println(array[idx]);
        }

        for (int value : array) {
            System.out.println(value); // seems like python
        }
    }
}

package streamapi;

import java.util.Arrays;
import java.util.List;

public class SumOfSquaresExample {
    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6);
        int sum = nums.stream().map(n -> n * n).reduce(0, Integer::sum);
        System.out.println("Sum of squares: " + sum);
    }
}

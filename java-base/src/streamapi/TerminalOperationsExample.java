package streamapi;

import java.util.Arrays;
import java.util.List;

public class TerminalOperationsExample {
    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 7);
        long count = nums.stream().filter(n -> n % 2 == 0).count();
        System.out.println("Number of even numbers: " + count);
    }
}

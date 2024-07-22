package streamapi;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

public class MaximumValueExample {
    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 7);
        Optional<Integer> max = nums.stream().max(Integer::compare);
        max.ifPresent(value -> System.out.println("Maxvalue: " + value));
    }
}

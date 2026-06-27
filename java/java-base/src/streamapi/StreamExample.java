package streamapi;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamExample {
    public static void main(String[] args) {
        List<Integer> ages = Arrays.asList(3, 4, 5, 10);
        List<Integer> oddAges = ages.stream().filter(n -> n % 2 != 0).map(n -> n * n).collect(Collectors.toList());
        System.out.println("Squared odd ages: " + oddAges);
    }
}

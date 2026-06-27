package streamapi;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class IntermediateOperationsExample {
    public static void main(String[] args) {
        List<String> cats = Arrays.asList("Loi", "Kitty", "Meo");
        List<String> catsShortname = cats.stream()
                .filter(n -> n.length() < 6)
                .map(String::toUpperCase)
                .collect(Collectors.toList());
        System.out.println("Result: " + catsShortname);
    }
}

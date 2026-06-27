package streamapi;

import java.util.List;
import java.util.Arrays;

public class LoopToForEachExample {
    public static void main(String[] args) {
        List<String> cats = Arrays.asList("Kitty", "Meo", "Shower");
        cats.forEach(s -> System.out.println(s));
    }
}

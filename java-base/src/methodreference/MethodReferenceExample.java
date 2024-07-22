package methodreference;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class MethodReferenceExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Luby", "Daisy", "Pandy");
        List<String> uppercaseNames = names.stream().map(String::toUpperCase).collect(Collectors.toList());
        System.out.println("Upper case names: " + uppercaseNames);
    }
}

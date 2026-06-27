package generics;

public class Main {
    public static void main(String[] args) {
        Box<Integer> intengerBox = new Box<>();
        intengerBox.setContent(42);

        Box<String> stringBox = new Box<>();
        stringBox.setContent("Universe");
    }
}

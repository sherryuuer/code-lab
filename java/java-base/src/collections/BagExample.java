package collections;

public class BagExample {
    public static void main(String[] args) {
        Bag<String> stringBag = new Bag<>();
        stringBag.addItem("Apple");
        stringBag.addItem("Orange");
        stringBag.removeItem("Orange");

        Bag<Integer> integerBag = new Bag<>();
        integerBag.addItem(1);
        integerBag.addItem(2);
        integerBag.removeItem(2);
    }
}

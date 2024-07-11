public class Methods {
    public static void main(String[] args) {
        greet();
        int res = add(1, 2);
        System.out.println(res);
    }

    public static void greet() {
        System.out.println("Hello!");
    }

    public static int add(int a, int b) {
        return a + b;
    }
}

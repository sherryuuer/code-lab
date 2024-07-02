public class Factorial {
    public static void main(String[] args) {
        System.out.println(factorial(3));
    }

    private static int factorial(int num) {
        if (num == 0) {
            return 1;
        }

        return factorial(num - 1) * num;
    }
}

public class loop_while {
    public static void main(String[] args) {
        int n = 1;

        while (n <= 10) {
            System.out.println(n);
            n = n + 1;
        }

        // get avarage
        int[] array = new int[] { 98, 12, 9, 102, 88 };
        int res = 0;
        int i = 0;
        while (i <= array.length - 1) {
            res = res + array[i];
            i = i + 1;
        }

        System.out.println(res / array.length);
    }
}

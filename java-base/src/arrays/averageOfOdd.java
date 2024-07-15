package arrays;

public class averageOfOdd {
    public static void main(String[] args) {
        int[] array = { 23, 4, 343, 89, 9, 68, 2 };
        int sum = 0;
        int count = 0;

        for (int num : array) {
            if (num % 2 == 0) {
                sum += num;
                count++;
            }
        }

        double res = (double) sum / count;
        System.out.println("the res is " + res);
    }
}

package arrays;

public class Primitives_Arrays_Casting {
    public static void main(String[] arges) {
        int a = 5;
        int b = 10;
        System.out.println(a + b);

        float x = 3.14f;
        float y = 2.22f;
        float sum = x + y;
        System.out.println("sum: " + sum);

        String str1 = "Hello, ";
        String str2 = "World!";
        String str = str1 + str2;
        System.out.println(str);

        int[] array = { 1, 2, 3, 4, 5 };
        System.out.println(array[0]);

        String text = "Java Programming";
        int text_length = text.length();
        System.out.println("The length of the string is " + text_length);

        double num = 3.14;
        int double_num = (int) num;
        System.out.println("Double number: " + double_num);

        int num2 = 10;
        num2 = modifyNumber(num2);
        System.out.println(num2);
    }

    public static int modifyNumber(int num) {
        return num * 2;
    }
}

/*
 * 15
 * sum: 5.36
 * Hello, World!
 * 1
 * The length of the string is 16
 * Double number: 3
 */

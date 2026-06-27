package strings;

public class StringExample {
    public static void main(String[] args) {
        String str1 = "nuts";
        String str2 = "beef";
        String str3 = "Hello, world!";

        System.out.println(str1 + " " + str2);
        System.out.println(str3.length());
        System.out.println(str3.toLowerCase());
        System.out.println(str3.toUpperCase());
        System.out.println(str3.substring(7, 12));
        System.out.println(str3.replace("world", "Java"));
    }
}

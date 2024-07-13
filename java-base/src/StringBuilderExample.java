public class StringBuilderExample {
    public static void main(String[] args) {
        StringBuilder sb1 = new StringBuilder("nuts");
        StringBuilder sb2 = new StringBuilder("nuts");

        System.out.println(sb1.toString().equals(sb2.toString())); // different object

        sb1.append(sb2);
        System.out.println(sb1);

        sb1.reverse();
        System.out.println(sb1);

    }
}

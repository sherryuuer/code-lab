public class hello_world {
    public static void main(String[] args) {
        final int a = 123; // 定数
        char b = 'A'; // unicode 65
        String c;
        c = "Hello"; //

        System.out.println(c + " World");
        System.out.println(a + b); // 188

        String pre;
        pre = "You&";
        System.out.print(pre);
        String post;
        post = "Me";
        System.out.println(post);

        // 计算取模
        int x;
        int y;

        x = 50;
        y = x % 23;

        System.out.println(y);

    }
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person();
        System.out.println(p.name);

        System.out.println(Counter.count);
        Counter.increment();
        System.out.println(Counter.count);

    }
}

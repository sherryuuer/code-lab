package concurrency;

public class SharedCounterDemo {
    static int counter = 0;

    // synchronized key word
    static synchronized void increment() {
        int current = counter;
        System.out.println("Before: " + counter);
        counter = current + 1;
        System.out.println("After: " + counter);
    }

    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            increment();
        });
        Thread t2 = new Thread(() -> {
            increment();
        });

        t1.start();
        t2.start();
    }
}

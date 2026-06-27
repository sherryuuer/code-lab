package concurrency;

public class BasicThreadCreation {
    public static void main(String[] args) {
        Thread myThread = new Thread(() -> {
            System.out.println("Hello from my thread!");
        });

        myThread.start();
    }
}

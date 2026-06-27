package concurrency;

public class RunnableInterfaceDemo {

    public static class NumberPrinter implements Runnable {
        @Override
        public void run() {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Print num: " + i);
            }
        }
    }

    public static void main(String[] args) {
        Thread myThread = new Thread(new NumberPrinter());
        myThread.start();
    }
}

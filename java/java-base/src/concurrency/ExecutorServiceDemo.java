package concurrency;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorServiceDemo {
    public static void main(String[] args) {
        ExecutorService fixedThreadPool = Executors.newFixedThreadPool(2);
        // 提交多个任务
        for (int i = 0; i < 5; i++) {
            final int index = i;
            fixedThreadPool.submit(() -> {
                System.out.println("Task " + index + " executed by: " + Thread.currentThread().getName());
            });
        }
        // 关闭线程池
        fixedThreadPool.shutdown();
    }
}

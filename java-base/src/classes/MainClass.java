package classes;

public class MainClass {
    public static void main(String[] args) {
        SubClass sub = new SubClass();
        sub.add(5, 7);

        staticSubClass.add(3, 7);
    }
}

// 静态方法可以直接通过类调用，非静态方法需要实例化后调用

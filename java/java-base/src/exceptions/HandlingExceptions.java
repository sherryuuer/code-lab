package exceptions;

public class HandlingExceptions {
    public static void main(String[] args) {
        try {
            ThrowingExceptions.validateNumber(-1);
        } catch (IllegalAccessError e) {
            System.out.println(e.getMessage());
        }
    }
}

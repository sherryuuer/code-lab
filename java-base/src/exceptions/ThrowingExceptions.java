package exceptions;

public class ThrowingExceptions {
    public static void validateNumber(int arg) {
        if (arg <= 0) {
            // checked exception 不需要方法throws异常
            throw new IllegalArgumentException("The argument must be non-negative.");
        }
    }
}

package exceptions;

public class CheckedVsUnchecked {
    public static void validateString(String s) throws EmptyStringException {
        if (s.isEmpty()) {
            // unchecked exception 需要在方法上throws异常
            throw new EmptyStringException("The string is empty.");
        }
    }
}

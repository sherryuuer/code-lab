package exceptions;

public class EmptyStringException extends Exception {
    public EmptyStringException() {
        super();
    }

    public EmptyStringException(String message) {
        super(message);
    }

    public EmptyStringException(Exception e) {
        super(e);
    }

}

package exceptions;

public class CustomCheckedException {
    public static void main(String[] args) {
        try {
            validateAge(150);
        } catch (InvalidAgeException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void validateAge(int age) throws InvalidAgeException {
        if (age < 0 || age > 120) {
            throw new InvalidAgeException("That is not a real age.");
        }
    }
}

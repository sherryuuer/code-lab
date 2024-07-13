import java.time.LocalDateTime;;

public class LocalDateTimeExampl {
    public static void main(String[] args) {
        // November 21 of 2023 at 6PM (18.00).
        LocalDateTime eventTime = LocalDateTime.of(2023, 11, 21, 18, 00);
        System.out.println(eventTime);
    }
}

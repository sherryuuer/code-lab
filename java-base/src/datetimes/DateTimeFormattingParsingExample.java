package datetimes;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeFormattingParsingExample {
    public static void main(String[] args) {
        // datetime to string
        LocalDateTime localDateTime = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        // String formattedDateTime = dtf.format(localDateTime);
        String formattedDateTime = localDateTime.format(dtf);
        System.out.println("The formatted date time is " + formattedDateTime);

        // string to datetime
        DateTimeFormatter dtfParse = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate localDate = LocalDate.parse("2023-11-21", dtfParse);
        System.out.println("The parsed date time is " + localDate);
    }
}

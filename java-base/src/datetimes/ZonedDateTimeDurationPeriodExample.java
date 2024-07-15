package datetimes;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.Period;
import java.time.ZonedDateTime;

public class ZonedDateTimeDurationPeriodExample {
    public static void main(String[] args) {
        LocalDateTime localTime = LocalDateTime.now();
        ZonedDateTime overseasEvent = ZonedDateTime.of(localTime, ZoneId.of("Asia/Tokyo"));
        System.out.println("The overseas event will be hold at " + overseasEvent);

        LocalTime lt1 = LocalTime.of(9, 0);
        LocalTime lt2 = LocalTime.of(17, 0);
        Duration dr = Duration.between(lt1, lt2);
        System.out.println("Duration: " + dr);

        LocalDate ld1 = LocalDate.of(2023, 1, 1);
        LocalDate ld2 = LocalDate.of(2023, 12, 31);
        Period pd = Period.between(ld1, ld2);
        System.out.println("Period: " + pd);
    }
}

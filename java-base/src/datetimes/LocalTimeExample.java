package datetimes;

import java.time.LocalTime;

public class LocalTimeExample {
    public static void main(String[] args) {
        LocalTime meetingTime = LocalTime.of(13, 30);
        System.out.println(meetingTime);
    }
}

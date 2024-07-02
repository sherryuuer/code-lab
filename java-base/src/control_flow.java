import java.util.Calendar;

public class control_flow {
    public static void main(String[] args) {
        int ret;
        int age = 4;
        String value = "OK";

        // age example
        if (age <= 3 && value.equals("OK")) { // String equals
            ret = 100;
        } else if (age <= 9) {
            ret = 300;
        } else {
            ret = 500;
        } // ||:or &&:and ==:equal

        System.out.println(ret);

        // calander
        Calendar calendar = Calendar.getInstance();
        int month = calendar.get(Calendar.MONTH) + 1;

        String monthName = "";

        if (month == 1) {
            monthName = "January";
        }
        if (month == 2) {
            monthName = "February";
        }
        if (month == 3) {
            monthName = "March";
        }
        if (month == 4) {
            monthName = "April";
        }
        if (month == 5) {
            monthName = "May";
        }
        if (month == 6) {
            monthName = "June";
        }
        if (month == 7) {
            monthName = "July";
        }
        if (month == 8) {
            monthName = "August";
        }
        if (month == 9) {
            monthName = "September";
        }
        if (month == 10) {
            monthName = "October";
        }
        if (month == 11) {
            monthName = "November";
        }
        if (month == 12) {
            monthName = "December";
        }

        System.out.println(monthName);

        // get the largest number in 3 nums
        int num1 = 54;
        int num2 = 31;
        int num3 = -100;
        int result;

        if (num1 > num2 && num1 > num3) {
            result = num1;
        } else if (num2 > num3) {
            result = num2;
        } else {
            result = num3;
        }

        System.out.println(result);

        // complax logic practice
        int kokugo;
        int sugaku;
        int eigo;
        int rika;
        int syakai;

        kokugo = 82;
        sugaku = 90;
        eigo = 73;
        rika = 79;
        syakai = 87;

        if (kokugo >= 80 && eigo >= 70) {
            System.out.println("合格");
        } else if (sugaku >= 70 && rika >= 80) {
            System.out.println("合格");
        } else if (syakai >= 80 && rika >= 80) {
            System.out.println("合格");
        } else if ((kokugo + sugaku + eigo + rika + syakai) >= 400) {
            System.out.println("合格");
        } else {
            System.out.println("不合格");
        }
    }

    // 全局变量：一般不推介使用，因为很难debug
    int result = fee(5);

    // function 练习
    private static int fee(int age) {
        int ret;

        if (age <= 3) {
            ret = 100;
        } else if (age <= 9) {
            ret = 300;
        } else {
            ret = 500;
        }

        return ret;
    }
}

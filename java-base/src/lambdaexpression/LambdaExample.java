package lambdaexpression;

import functionalinterface.*;

public class LambdaExample {
    public static void main(String[] args) {
        NumericOperator addition = (x, y) -> x + y;
        int sum = addition.operate(1, 2);
        System.out.println("Sum: " + sum);

        NumericOperator maximum = (x, y) -> (x > y) ? x : y;
        int max = maximum.operate(2, 3);
        System.out.println("Max: " + max);

        StringFormatter uppercase = x -> x.toUpperCase();
        String uppeString = uppercase.format("Sally");
        System.out.println("Uppercase: " + uppeString);

    }
}

public class Exercise {
    public static void main(String[] args) {
        Circle circle = new Circle();
        Square square = new Square();
        Triangle triangle = new Triangle();

        circle.setRadius(10);
        square.setHeight(32);
        square.setWidth(12);
        triangle.setBottom(20);
        triangle.setHeight(8);

        double[] area = new double[] {
                circle.getArea(),
                square.getArea(),
                triangle.getArea(),
        };

        double result = 0;

        for (double x : area) {
            result = result + x;
        }

        System.out.println(result);
    }
}

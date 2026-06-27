package constructors;

public class Vehicle {
    private String brand;

    public Vehicle(String brand) {
        this.brand = brand;
    }

    public void print() {
        System.out.println(brand);
    }
}

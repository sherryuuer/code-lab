package constructors;

public class DefaultConstructorExample {
    public static void main(String[] args) {
        // because the Vehicle's constructor has parameter, this will cause error
        // Vehicle vehicle = new Vehicle();
        Vehicle vehicle = new Vehicle(null);
        System.out.println("Object" + vehicle + "created.");
    }
}

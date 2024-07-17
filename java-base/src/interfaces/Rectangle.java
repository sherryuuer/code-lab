package interfaces;

public class Rectangle implements Drawable, Countable {
    @Override
    public void draw() {
        System.out.println("Draw.");
    }

    @Override
    public void printInfo() {
        System.out.println("Rectangle info.");
    }
}

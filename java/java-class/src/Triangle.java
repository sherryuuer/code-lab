public class Triangle {
    int height;
    int bottom;

    public void setHeight(int val) {
        height = val;
    }

    public void setBottom(int val) {
        bottom = val;
    }

    public double getArea() {
        return height * bottom / 2;
    }

}

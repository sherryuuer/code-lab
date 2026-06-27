package enumstype;

public enum Planet {
    MERCURY("Mercury", 0.39),
    VENUS("Venus", 0.72),
    EARTH("Earth", 1.0),
    MARS("Mars", 1.52),
    JUPITER("Jupiter", 5.20),
    SATURN("Saturn", 9.58),
    URANUS("Uranus", 19.22),
    NEPTUNE("Neptune", 30.05);

    private final String name;
    private final double distanceFromSun;

    Planet(String name, double distanceFromSun) {
        this.name = name;
        this.distanceFromSun = distanceFromSun;
    }

    public String getName() {
        return name;
    }

    public double getDistanceFromSun() {
        return distanceFromSun;
    }
}

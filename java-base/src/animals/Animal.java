package animals;

public class Animal {
    protected String species = "x";
    // 想要被另一个包中的子类Dog访问就需要protected
    // 或者把Dog类放进这边的Animal包里，就不需要protected
}

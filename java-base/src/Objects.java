public class Objects {
    public static void main(String[] args) {
        Person person = new Person();
        person.name = "Evie";
        person.age = 36;

        Car car = new Car();
        car.model = "86";
        car.owner = person;

        updatePerson(person);

        System.out.println("My friend " + person.name + " is " + person.age + " years old.");
        System.out.println("He has a car of model " + car.model + ".");
    }

    public static void updatePerson(Person p) {
        p.name = "Sally";
        p.age = 35;
    }
}

class Car {
    String model;
    Person owner;
}

class Person {
    String name;
    int age;

}

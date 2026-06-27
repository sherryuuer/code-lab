package oop;

public class Animal {
    private String sound;

    // Constructor
    public Animal(String sound) {
        setSound(sound);
    }

    public String getSound() {
        return sound;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    public void makeSound() {
        System.out.println("Animal Sound: " + getSound());
    }
}

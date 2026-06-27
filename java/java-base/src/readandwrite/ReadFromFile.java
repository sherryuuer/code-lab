package readandwrite;

import java.io.FileReader;
import java.io.IOException;
// import java.io.FileNotFoundException;

public class ReadFromFile {
    public static void readFile(String filepath) {
        try (FileReader fr = new FileReader(filepath)) {
            int character;
            while ((character = fr.read()) != -1) {
                System.out.println((char) character);
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}

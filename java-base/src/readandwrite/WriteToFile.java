package readandwrite;

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

public class WriteToFile {
    public static void writeNames(String filepath, String[] names) throws FileNotFoundException {
        try (FileWriter fw = new FileWriter(filepath)) {
            for (String name : names) {
                fw.write(name + "\n");
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}

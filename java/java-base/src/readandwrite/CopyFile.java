package readandwrite;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;

public class CopyFile {
    public static void copyFile(String sourcePath, String destinationPath) throws FileNotFoundException {
        try (FileReader fr = new FileReader(sourcePath);
                FileWriter fw = new FileWriter(destinationPath)) {
            int data;
            while ((data = fr.read()) != -1) {
                fw.write(data);
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        try {
            copyFile("sourcefile.txt", "destinationfile.txt");
            System.out.println("Success!");
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        }
    }
}

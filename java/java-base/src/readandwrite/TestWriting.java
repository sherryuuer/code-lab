package readandwrite;

import java.io.FileNotFoundException;

public class TestWriting {
    public static void main(String[] args) throws FileNotFoundException {
        String filepath = "test.txt";
        String[] names = new String[] { "Sunny", "Jack", "Luby" };
        WriteToFile.writeNames(filepath, names);
    }
}

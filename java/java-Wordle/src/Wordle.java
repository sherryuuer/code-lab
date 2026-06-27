import java.util.Scanner;

public class Wordle {
    private String secretWord;
    private int attempts;

    public Wordle(String secretWord, int attempts) {
        this.secretWord = secretWord;
        this.attempts = attempts;
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        int remainedAttmpts = attempts;

        System.out.println("The secret word include " + secretWord.length() + " characters.");

        while (remainedAttmpts > 0) {
            System.out.println("Enter your guess: ");
            String guess = scanner.nextLine();

            // check if the length is not match
            if (guess.length() != secretWord.length()) {
                System.out.println("Invalid guess. Please try again with the right length as the secret word.");
            }

            int correctChars = 0;
            int correctPositions = 0;

            // check the guess and get the datas
            for (int i = 0; i < secretWord.length(); i++) {
                char c = guess.charAt(i);
                if (c == secretWord.charAt(i)) {
                    correctPositions++;
                }
                if (secretWord.indexOf(c) >= 0) {
                    correctChars++;
                }
            }

            if (correctPositions == secretWord.length()) {
                System.out.println("Congratulations! You guessed the secret word: " + secretWord);
                break;
            } else {
                System.out.println("Correct characters: " + correctChars);
                System.out.println("Correct positions: " + correctPositions);
                remainedAttmpts--;
            }
        }

        if (remainedAttmpts == 0) {
            System.out.println("Sorry, you are out of attempts. The secret word is: " + secretWord);
        }

        scanner.close();
    }
}

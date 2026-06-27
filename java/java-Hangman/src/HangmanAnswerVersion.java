import java.util.HashSet;
import java.util.Scanner;

public class HangmanAnswerVersion {
    private String secretWord;
    private int attempts;
    private StringBuilder guessedWord;
    private HashSet<Character> guessedLetters;

    public HangmanAnswerVersion(String secretWord, int attempts) {
        this.secretWord = secretWord;
        this.attempts = attempts;
        this.guessedWord = new StringBuilder(secretWord.replaceAll(".", "_"));
        this.guessedLetters = new HashSet<>();
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        int remainedAttmpts = attempts;

        while (remainedAttmpts > 0 && !guessedWord.toString().equals(secretWord)) {
            System.out.println("Attempts remaining: " + remainedAttmpts);
            System.out.println("Guessed word: " + guessedWord);
            System.out.println("Enter your guess: ");
            char guess = scanner.next().charAt(0);

            // if invalid guess
            if (guessedLetters.contains(guess)) {
                System.out.println("You've guessed the letter.");
                continue;
            }

            guessedLetters.add(guess);

            // if the letter not in the word
            if (secretWord.indexOf(guess) >= 0) {
                // update the guessedWord
                for (int i = 0; i < secretWord.length(); i++) {
                    if (guess == secretWord.charAt(i)) {
                        guessedWord.setCharAt(i, guess);
                    }
                }
            } else {
                remainedAttmpts--;
            }

            // if the guessed word equals the secretWord
            if (guessedWord.toString().equals(secretWord)) {
                System.out.println("You won, the secret word is " + secretWord);
            } else {
                System.out.println("You lose, the secret word is " + secretWord);
            }
        }

        scanner.close();
    }
}

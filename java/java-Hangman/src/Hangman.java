import java.util.HashSet;
import java.util.Scanner;

public class Hangman {
    private String secretWord;
    private int attempts;
    private StringBuilder guessedWord = new StringBuilder();
    private HashSet<Character> guessedLetters = new HashSet<>();

    public Hangman(String secretWord, int attempts) {
        this.secretWord = secretWord;
        this.attempts = attempts;

        for (int i = 0; i < secretWord.length(); i++) {
            guessedWord.append('_');
        }
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        int remainedAttmpts = attempts;
        boolean gameOver = false;

        System.out.println("Welcome to the Hangman Game!");
        while (!gameOver) {
            System.out.println("Enter your guess: ");
            char guess = scanner.next().charAt(0);

            // if invalid guess
            if (guessedLetters.contains(guess)) {
                System.out.println("You've guessed the letter.");
                continue;
            }

            guessedLetters.add(guess);

            // update the guessedWord
            for (int i = 0; i < secretWord.length(); i++) {
                if (guess == secretWord.charAt(i)) {
                    guessedWord.setCharAt(i, guess);
                }
            }
            System.out.println("You guessed: " + guessedWord);

            // if the letter not in the word
            if (secretWord.indexOf(guess) == -1) {
                remainedAttmpts--;
                System.out.println("Wrong letter, your remain " + remainedAttmpts + " attmpts.");
                if (remainedAttmpts == 0) {
                    gameOver = true;
                    System.out.println("You lose.");
                }
            }

            // if the guessed word equals the secretWord
            if (guessedWord.toString().equals(secretWord)) {
                gameOver = true;
                System.out.println("You won.");
            }
        }

        scanner.close();
    }
}

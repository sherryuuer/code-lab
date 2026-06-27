import java.util.Scanner;

public class Trivia {
    private int score;

    public Trivia() {
        this.score = 0;
    }

    public void play(Question[] questions) {
        Scanner scanner = new Scanner(System.in);
        ;
        for (int i = 0; i < questions.length; i++) {
            Question question = questions[i];
            System.out.println("Question " + (i + 1) + ": " + question.getQueation());
            String[] options = question.getOptions();
            for (int j = 0; j < options.length; j++) {
                System.out.println((j + 1) + ". " + options[j]);
            }

            System.out.println("Enter your answer: (1 - " + options.length + "): ");
            int answer = scanner.nextInt() - 1;

            if (question.isCorrectAnswer(answer)) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Incorrect!");
            }
        }

        System.out.println("Your final score is " + score + " out of " + questions.length);

        scanner.close();
    }
}

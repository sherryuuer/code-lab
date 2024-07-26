public class TriviaGame {
    public static void main(String[] args) {
        Question[] questions = {
                new Question("1 + 1 = ?", new String[] { "1", "2", "3" }, 1),
                new Question("2 + 3 = ?", new String[] { "3", "4", "5" }, 2),
        };

        Trivia game = new Trivia();
        game.play(questions);
    }
}

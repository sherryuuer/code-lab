import java.util.Arrays;

public class transformMatrix {
    public static void main(String[] args) {
        int[][] array = new int[][] {
                { 3, 0, 0, 0, 0 },
                { 0, 2, 2, 0, 0 },
                { 0, 0, 0, 1, 3 },
                { 0, 0, 0, 2, 0 },
                { 0, 0, 0, 0, 1 },
        };
        int[][] res = transformSparseMatrix(array);
        for (int idx = 0; idx <= array.length - 1; idx++) {
            System.out.println(Arrays.toString(res[idx]));
        }
    }

    private static int[][] transformSparseMatrix(int[][] matrix) {
        int i, j;
        int[][] sparseMatrix = new int[3][10];
        int tail = 0;

        for (i = 0; i <= matrix.length - 1; i++) {
            for (j = 0; j <= matrix[0].length - 1; j++) {
                if (matrix[i][j] != 0) {
                    sparseMatrix[0][tail] = i;
                    sparseMatrix[1][tail] = j;
                    sparseMatrix[2][tail] = matrix[i][j];
                    tail++;
                }
            }
        }

        return sparseMatrix;
    }
}

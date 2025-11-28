// Leetcode 1738: Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
// Solved on 28th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Finds the k-th largest XOR coordinate value in a given matrix.
     *
     * @param matrix The input 2D integer array.
     * @param k The k-th largest value to find.
     * @return The k-th largest XOR coordinate value.
     */
    public int kthLargestValue(int[][] matrix, int k) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[] coordinates = new int[rows * cols];
        int index = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (i > 0) {
                    matrix[i][j] ^= matrix[i - 1][j];
                }
                if (j > 0) {
                    matrix[i][j] ^= matrix[i][j - 1];
                }
                if (i > 0 && j > 0) {
                    matrix[i][j] ^= matrix[i - 1][j - 1];
                }
                
                coordinates[index++] = matrix[i][j];
            }
        }

        Arrays.sort(coordinates);
        return coordinates[coordinates.length - k];
    }
}
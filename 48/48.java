// Leetcode 48: Rotate Image
// https://leetcode.com/problems/rotate-image/
// Solved on 4th of May, 2026
class Solution {
    /**
     * Rotates the image by 90 degrees (clockwise) in-place.
     * 
     * @param matrix A 2D square matrix representing an image.
     */
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
}
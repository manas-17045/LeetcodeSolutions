// Leetcode 1727: Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/
// Solved on 17th of March, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the area of the largest submatrix that can be formed by rearranging columns.
     *
     * @param matrix A binary matrix of size m x n.
     * @return The area of the largest submatrix containing only 1s.
     */
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }
        int maxArea = 0;
        for (int i = 0; i < m; i++) {
            Arrays.sort(matrix[i]);
            for (int j = n - 1; j >= 0; j--) {
                int area = matrix[i][j] * (n - j);
                maxArea = Math.max(maxArea, area);
            }
        }
        return maxArea;
    }
}
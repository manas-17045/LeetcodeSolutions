// Leetcode 3867: Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/
// Solved on 20th of March, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum absolute difference between any two distinct elements 
     * within every sliding k x k submatrix of the given grid.
     * 
     * @param grid The input 2D integer array.
     * @param k The size of the square submatrix.
     * @return A 2D array where each element [i][j] is the minimum absolute difference in the submatrix starting at (i, j).
     */
    public int[][] minAbsDiff(int[][] grid, int k) {
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] result = new int[rows - k + 1][cols - k + 1];
        int[] values = new int[k * k];

        for (int i = 0; i < rows - k; i++) {
            for (int j = 0; j <= cols - k; j++) {
                int index = 0;
                for (int r = i; r < i + k; r++) {
                    for (int c = j; c < j + k; c++) {
                        values[index++] = grid[r][c];
                    }
                }

                Arrays.sort(values);
                int minDiff = Integer.MAX_VALUE;

                for (int x = 1; x < values.length; x++) {
                    if (values[x] != vaalues[x - 1]) {
                        int diff = values[x] - values[x - 1];
                        if (diff < minDiff) {
                            minDiff = diff;
                        }
                    }
                }

                if (minDiff == Integer.MAX_VALUE) {
                    result[i][j] = 0;
                } else {
                    result[i][j] = minDiff;
                }
            }
        }
        return result;
    }
}
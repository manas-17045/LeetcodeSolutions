// Leetcode 1292: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
// Solved on 19th of January, 2026
class Solution {
    /**
     * Finds the maximum side length of a square subgrid whose sum is less than or equal to the given threshold.
     * @param mat The input 2D integer array representing the grid.
     * @param threshold The maximum allowed sum for a square subgrid.
     * @return The maximum side length of a square subgrid that satisfies the condition.
     */
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] sum = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }

        int maxSide = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int len = maxSide + 1;
                if (i >= len - 1 && j >= len - 1) {
                    int currentSum = sum[i + 1][j + 1] - sum[i + 1 - len][j + 1] - sum[i + 1][j + 1 - len] + sum[i + 1 - len][j + 1 - len];
                    if (currentSum <= threshold) {
                        maxSide++;
                    }
                }
            }
        }
        return maxSide;
    }
}
// Leetcode 3070: Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Counts the number of submatrices with a top-left element (0,0) and a sum less than or equal to k.
     * @param grid The input 2D array (matrix).
     * @param k The maximum allowed sum for a submatrix.
     * @return The total count of submatrices satisfying the conditions.
     */
    public int countSubmatrices(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        int[][] prefixSum = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    prefixSum[i][j] = grid[i][j];
                } else if (i == 0) {
                    prefixSum[i][j] = prefixSum[i][j - 1] + grid[i][j];
                } else if (j == 0) {
                    prefixSum[i][j] = prefixSum[i - 1][j] + grid[i][j];
                } else {
                    prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + grid[i][j];
                }

                if (prefixSum[i][j] <= k) {
                    count++;
                }
            }
        }

        return count;
    }
}
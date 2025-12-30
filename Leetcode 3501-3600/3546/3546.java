// Leetcode 3546: Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Checks if the given grid can be partitioned into two sub-grids with equal sums.
     * A partition can be either a horizontal cut or a vertical cut.
     * @param grid The input 2D integer array (grid).
     * @return True if the grid can be partitioned into two sub-grids with equal sums, false otherwise.
     */
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long total = 0;
        long[] rowSum = new long[m];
        long[] colSum = new long[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                total += val;
                rowSum[i] += val;
                colSum[j] += val;
            }
        }

        if (total % 2 != 0) {
            return false;
        }

        long target = total / 2;
        long current = 0;

        for (int i = 0; i < m - 1; i++) {
            current += rowSum[i];
            if (current == target) {
                return true;
            }
        }

        current = 0;
        for (int j = 0; j < n - 1; j++) {
            current += colSum[j];
            if (current == target) {
                return true;
            }
        }

        return false;
    }
}
// Leetcode 3122: Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/
// Solved on 6th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to satisfy the given conditions.
     * The conditions are that in each column, all elements must be the same, and
     * adjacent columns must have different elements.
     * @param grid The input 2D integer array representing the grid.
     * @return The minimum number of operations required.
     */
    public int minimumOperations(int[][] grid) {
        if (grid == null) {
            return 0;
        }
        int rows = grid.length;
        if (rows == 0) {
            return 0;
        }
        int cols = grid[0].length;
        if (cols == 0) {
            return 0;
        }
        int[][] counts = new int[cols][10];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                counts[j][grid[i][j]]++;
            }
        }
        int[] dpPrev = new int[10];
        for (int d = 0; d < 10; d++) {
            dpPrev[d] = rows - counts[0][d];
        }
        for (int c = 1; c < cols; c++) {
            int min1 = Integer.MAX_VALUE;
            int min2 = Integer.MAX_VALUE;
            int minIdx = -1;
            for (int d = 0; d < 10; d++) {
                int v = dpPrev[d];
                if (v < min1) {
                    min2 = min1;
                    min1 = v;
                    minIdx = d;
                } else if (v < min2) {
                    min2 = v;
                }
            }
            int[] dpCurr = new int[10];
            for (int d = 0; d < 10; d++) {
                int base = rows - counts[c][d];
                dpCurr[d] = base + (d == minIdx ? min2 : min1);
            }
            dpPrev = dpCurr;
        }
        int res = Integer.MAX_VALUE;
        for (int d = 0; d < 10; d++){
            if (dpPrev[d] < res){
                res = dpPrev[d];
            }
        }
        return res;
    }
}
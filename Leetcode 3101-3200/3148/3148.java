// Leetcode 3148: Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/
// Solved on 9th of December, 2025
class Solution {
    /**
     * Calculates the maximum difference score in a grid.
     * The score is defined as the maximum value of grid[r2][c2] - grid[r1][c1]
     * where r2 >= r1 and c2 >= c1, and (r1, c1) != (r2, c2).
     * @param grid The input grid of integers.
     * @return The maximum difference score.
     */
    public int maxScore(List<List<Integer>> grid) {
        int rows = grid.size();
        int cols = grid.get(0).size();
        int result = Integer.MIN_VALUE;
        int[] minValues = new int[cols];
        
        for (int j = 0; j < cols; j++) {
            minValues[j] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < rows; i++) {
            List<Integer> currentRow = grid.get(i);
            for (int j = 0; j < cols; j++) {
                int val = currentRow.get(j);
                int minPrev = Integer.MAX_VALUE;

                if (i > 0) {
                    minPrev = Math.min(minPrev, minValues[j]);
                }
                
                if (j > 0) {
                    minPrev = Math.min(minPrev, minValues[j - 1]);
                }

                if (minPrev != Integer.MAX_VALUE) {
                    result = Math.max(result, val - minPrev);
                }

                minValues[j] = Math.min(val, minPrev);
            }
        }
        
        return result;
    }
}
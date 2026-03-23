// Leetcode 1594: Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
// Solved on 23rd of March, 2026
class Solution {
    /**
     * Finds the maximum non-negative product of a path from (0, 0) to (rows-1, cols-1).
     * 
     * @param grid A 2D matrix of integers.
     * @return The maximum non-negative product modulo 10^9 + 7, or -1 if no such product exists.
     */
    public int maxProductPath(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        long[] maxRow = new long[cols];
        long[] minRow = new long[cols];
        
        maxRow[0] = grid[0][0];
        minRow[0] = grid[0][0];
        
        for (int j = 1; j < cols; j++) {
            maxRow[j] = maxRow[j - 1] * grid[0][j];
            minRow[j] = maxRow[j];
        }
        
        for (int i = 1; i < rows; i++) {
            maxRow[0] = maxRow[0] * grid[i][0];
            minRow[0] = maxRow[0];
            
            for (int j = 1; j < cols; j++) {
                long val = grid[i][j];
                long prevMax = Math.max(maxRow[j], maxRow[j - 1]);
                long prevMin = Math.min(minRow[j], minRow[j - 1]);
                
                if (val < 0) {
                    maxRow[j] = prevMin * val;
                    minRow[j] = prevMax * val;
                } else {
                    maxRow[j] = prevMax * val;
                    minRow[j] = prevMin * val;
                }
            }
        }
        
        long maxProd = maxRow[cols - 1];
        if (maxProd < 0) {
            return -1;
        }
        
        return (int) (maxProd % 1000000007);
    }
}
// Leetcode 1351: Count Negative Numbers in a Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
// Solved on 28th of December, 2025
class Solution {
    /**
     * Counts the number of negative numbers in a sorted matrix.
     * @param grid The input 2D array (matrix) sorted in non-increasing order both row-wise and column-wise.
     * @return The total count of negative numbers in the matrix.
     */
    public int countNegatives(int[][] grid) {
        int count = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        int row = rows - 1;
        int col = 0;

        while (row >= 0 && col < cols) {
            if (grid[row][col] < 0) {
                count += cols - col;
                row--;
            } else {
                col++;
            }
        }
        
        return count;
    }
}
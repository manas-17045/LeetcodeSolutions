// Leetcode 4052: Cyclically Shift Rows and Columns
// https://leetcode.com/problems/cyclically-shift-rows-and-columns/
// Solved on 15th of October, 2026
class Solution {
    /**
     * Shifts each row of the grid cyclically to the left and then shifts
     * each resulting column cyclically upward.
     *
     * @param n the dimension of the n x n grid
     * @param grid the initial square matrix
     * @param rowShift the cyclic left shift amount for each row
     * @param colShift the cyclic upward shift amount for each column
     * @return the transformed grid after row and column shifts
     */
    public int[][] cyclicShift(int n, int[][] grid, int[] rowShift, int[] colShift) {
        int[][] result = new int [n][n];

        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                int targetCol = (col - rowShift[row] + n) % n;
                int targetRow = (row - colShift[targetCol] + n) % n;
                result[targetRow][targetCol] = grid[row][col];
            }
        }

        return result;
    }
}
// Leetcode 3537: Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/
// Solved on 27th of October, 2025
class Solution {
    public int[][] specialGrid(int n) {
        /**
         * Fills a special grid of size 2^n x 2^n according to a specific pattern.
         * @param n The exponent determining the size of the grid (2^n x 2^n).
         * @return The filled 2D integer array representing the special grid.
         */
        int size = 1 << n;
        int[][] grid = new int[size][size];
        fillRecursive(grid, 0, 0, size, 0);
        return grid;
    }

    private void fillRecursive(int[][] grid, int row, int col, int size, int baseValue) {
        if (size == 1) {
            grid[row][col] = baseValue;
            return;
        }

        int newSize = size / 2;
        int quadrantValueCount = newSize * newSize;

        fillRecursive(grid, row, col + newSize, newSize, baseValue);
        fillRecursive(grid, row + newSize, col + newSize, newSize, baseValue + quadrantValueCount);
        fillRecursive(grid, row + newSize, col, newSize, baseValue + 2 * quadrantValueCount);
        fillRecursive(grid, row, col, newSize, baseValue + 3 * quadrantValueCount);
    }
}
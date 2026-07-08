// Leetcode 3963: Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/
// Solved on 8th of July, 2026
class Solution {
    /**
     * Creates a grid of size m x n with exactly one path from the top-left cell to 
     * the bottom-right cell.
     * @param m The number of rows in the grid.
     * @param n The number of columns in the grid.
     * @return A grid of size m x n with exactly one path from the top-left cell to 
     * the bottom-right cell.
     */
    public String[] createGrid(int m, int n) {
        String[] grid = new String[m];
        char[] firstRow = new char[n];
        for (int j = 0; j < n; j++) {
            firstRow[j] = '.';
        }
        grid[0] = new String(firstRow);
        
        for (int i = 1; i < m; i++) {
            char[] row = new char[n];
            for (int j = 0; j < n - 1; j++) {
                row[j] = '#';
            }
            row[n - 1] = '.';
            grid[i] = new String(row);
        }
        return grid;
    }
}
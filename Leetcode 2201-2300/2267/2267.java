// Leetcode 2267: Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
// Solved on 29th of September, 2026
class Solution {
    /**
     * Determines if there is a valid parentheses string path in the grid from the top-left to the bottom-right cell.
     *
     * @param grid the 2D character array representing the parentheses grid
     * @return true if a valid parentheses string path exists, false otherwise
     */
    public boolean hasValidPath(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        if ((rows + cols - 1) % 2 != 0 || grid[0][0] == ')' || grid[rows - 1][cols - 1] == '(') {
            return false;
        }
        boolean[][][] visited = new boolean[rows][cols][(rows + cols) / 2 + 1];
        return dfs(grid, 0, 0, 0, rows, cols, visited);
    }

    private boolean dfs(char[][] grid, int row, int col, int balance, int rows, int cols, boolean[][][] visited) {
        balance += grid[row][col] == '(' ? 1 : -1;
        if (balance < 0 || balance > (rows - 1 - row) + (cols - 1 - col)) {
            return false;
        }
        if (row == rows - 1 && col == cols - 1) {
            return balance == 0;
        }
        if (visited[row][col][balance]) {
            return false;
        }
        visited[row][col][balance] = true;
        if (row + 1 < rows && dfs(grid, row + 1, col, balance, rows, cols, visited)) {
            return true;
        }
        if (col + 1 < cols && dfs(grid, row, col + 1, balance, rows, cols, visited)) {
            return true;
        }
        return false;
    }
}
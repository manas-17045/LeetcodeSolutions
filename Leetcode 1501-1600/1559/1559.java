// Leetcode 1559: Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/
// Solved on 26th of April, 2026
class Solution {
    /**
     * Detects if there is a cycle of the same value in a 2D grid.
     * 
     * @param grid A 2D character array representing the grid.
     * @return true if a cycle exists, false otherwise.
     */
    public boolean containsCycle(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (!visited[i][j]) {
                    if (checkCycle(grid, visited, i, j, -1, -1, grid[i][j])) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
    private boolean checkCycle(char[][] grid, boolean[][] visited, int row, int col, int prevRow, int prevCol, char val) {
        visited[row][col] = true;
        
        int[] dirRow = {-1, 1, 0, 0};
        int[] dirCol = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            int nextRow = row + dirRow[i];
            int nextCol = col + dirCol[i];
            
            if (nextRow >= 0 && nextRow < grid.length && nextCol >= 0 && nextCol < grid[0].length) {
                if (grid[nextRow][nextCol] == val) {
                    if (nextRow != prevRow || nextCol != prevCol) {
                        if (visited[nextRow][nextCol]) {
                            return true;
                        }
                        if (checkCycle(grid, visited, nextRow, nextCol, row, col, val)) {
                            return true;
                        }
                    }
                }
            }
        }
        
        return false;
    }
}
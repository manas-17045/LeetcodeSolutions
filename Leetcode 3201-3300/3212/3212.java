// Leetcode 3212: Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
// Solved on 19th of March, 2026
class Solution {
    /**
     * Counts the number of submatrices starting from (0, 0) that contain 
     * an equal frequency of 'X' and 'Y', with at least one 'X'.
     * 
     * @param grid A 2D character array containing 'X', 'Y', or '.'.
     * @return The total number of valid submatrices.
     */
    public int numberOfSubmatrices(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int[] countX = new int[cols];
        int[] countY = new int[cols];
        int result = 0;
        
        for (int i = 0; i < rows; i++) {
            int rowX = 0;
            int rowY = 0;
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 'X') {
                    rowX++;
                } else if (grid[i][j] == 'Y') {
                    rowY++;
                }
                countX[j] += rowX;
                countY[j] += rowY;
                
                if (countX[j] == countY[j] && countX[j] > 0) {
                    result++;
                }
            }
        }
        
        return result;
    }
}
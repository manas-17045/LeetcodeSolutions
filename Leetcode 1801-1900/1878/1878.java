// Leetcode 1878: Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
// Solved on 16th of March, 2026
class Solution {
    /**
     * Finds the three biggest distinct rhombus sums in a grid.
     * 
     * @param grid A 2D integer array representing the grid.
     * @return An array containing the three largest distinct rhombus sums in descending order.
     */
    public int[] getBiggestThree(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int[] topThree = new int[] {-1, -1, -1};
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                updateLargest(topThree, grid[i][j]);
                
                int maxRadius = Math.min(Math.min(j, cols - 1 - j), (rows - 1 - i) / 2);
                for (int radius = 1; radius <= maxRadius; radius++) {
                    int currentSum = 0;
                    int currentRow = i;
                    int currentCol = j;
                    
                    for (int k = 0; k < radius; k++) {
                        currentSum += grid[currentRow][currentCol];
                        currentRow++;
                        currentCol--;
                    }
                    for (int k = 0; k < radius; k++) {
                        currentSum += grid[currentRow][currentCol];
                        currentRow++;
                        currentCol++;
                    }
                    for (int k = 0; k < radius; k++) {
                        currentSum += grid[currentRow][currentCol];
                        currentRow--;
                        currentCol++;
                    }
                    for (int k = 0; k < radius; k++) {
                        currentSum += grid[currentRow][currentCol];
                        currentRow--;
                        currentCol--;
                    }
                    
                    updateLargest(topThree, currentSum);
                }
            }
        }
        
        int validCount = 0;
        for (int value : topThree) {
            if (value != -1) {
                validCount++;
            }
        }
        
        int[] finalResult = new int[validCount];
        for (int i = 0; i < validCount; i++) {
            finalResult[i] = topThree[i];
        }
        
        return finalResult;
    }
    
    private void updateLargest(int[] topThree, int newValue) {
        if (newValue == topThree[0] || newValue == topThree[1] || newValue == topThree[2]) {
            return;
        }
        if (newValue > topThree[0]) {
            topThree[2] = topThree[1];
            topThree[1] = topThree[0];
            topThree[0] = newValue;
        } else if (newValue > topThree[1]) {
            topThree[2] = topThree[1];
            topThree[1] = newValue;
        } else if (newValue > topThree[2]) {
            topThree[2] = newValue;
        }
    }
}
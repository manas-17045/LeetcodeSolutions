// Leetcode 2033: Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
// Solved on 28th of April, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to make all elements in the grid equal.
     * In one operation, you can add or subtract x from any element.
     * 
     * @param grid A 2D integer array representing the grid.
     * @param x The integer value to add or subtract in a single operation.
     * @return The minimum operations required, or -1 if it's impossible.
     */
    public int minOperations(int[][] grid, int x) {
        int[] elementCounts = new int[10001];
        int remainder = -1;
        int totalElements = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                int currentValue = grid[i][j];
                if (remainder == -1) {
                    remainder = currentValue % x;
                } else if (currentValue % x != remainder) {
                    return -1;
                }
                elementCounts[currentValue]++;
                totalElements++;
            }
        }
        
        int medianValue = -1;
        int currentCount = 0;
        int targetCount = totalElements / 2;
        
        for (int i = 1; i <= 10000; i++) {
            if (elementCounts[i] > 0) {
                currentCount += elementCounts[i];
                if (currentCount > targetCount) {
                    medianValue = i;
                    break;
                }
            }
        }
        
        int totalOperations = 0;
        
        for (int i = 1; i <= 10000; i++) {
            if (elementCounts[i] > 0) {
                totalOperations += elementCounts[i] * (Math.abs(i - medianValue) / x);
            }
        }
        
        return totalOperations;
    }
}
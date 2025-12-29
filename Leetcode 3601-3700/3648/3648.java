// Leetcode 3648: Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/
// Solved on 29th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of sensors required to cover an n x m grid.
     * Each sensor has a range of k, meaning it covers a (2k+1) x (2k+1) square.
     * @param n The number of rows in the grid.
     * @param m The number of columns in the grid.
     * @param k The range of each sensor.
     * @return The minimum number of sensors needed.
     */
    public int minSensors(int n, int m, int k) {
        int range = 2 * k + 1;
        int rowsNeeded = (n + range - 1) / range;
        int colsNeeded = (m + range - 1) / range;
        
        return rowsNeeded * colsNeeded;
    }
}
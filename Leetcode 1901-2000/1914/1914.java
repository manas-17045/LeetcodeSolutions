// Leetcode 1914: Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/
// Solved on 9th of May, 2026
class Solution {
    /**
     * Cyclically rotates the layers of a grid counter-clockwise by k units.
     *
     * @param grid A 2D integer array representing the m x n matrix.
     * @param k    The number of times to rotate each layer cyclically.
     * @return     The modified grid after rotations.
     */
    public int[][] rotateGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int layers = Math.min(m, n) / 2;
        
        for (int layer = 0; layer < layers; layer++) {
            int top = layer;
            int bottom = m - 1 - layer;
            int left = layer;
            int right = n - 1 - layer;
            int len = 2 * (bottom - top + 1) + 2 * (right - left + 1) - 4;
            int[] temp = new int[len];
            int idx = 0;
            
            for (int j = left; j <= right; j++) {
                temp[idx++] = grid[top][j];
            }
            for (int i = top + 1; i <= bottom; i++) {
                temp[idx++] = grid[i][right];
            }
            for (int j = right - 1; j >= left; j--) {
                temp[idx++] = grid[bottom][j];
            }
            for (int i = bottom - 1; i > top; i--) {
                temp[idx++] = grid[i][left];
            }
            
            int shifts = k % len;
            idx = shifts;
            
            for (int j = left; j <= right; j++) {
                grid[top][j] = temp[idx];
                idx = (idx + 1) % len;
            }
            for (int i = top + 1; i <= bottom; i++) {
                grid[i][right] = temp[idx];
                idx = (idx + 1) % len;
            }
            for (int j = right - 1; j >= left; j--) {
                grid[bottom][j] = temp[idx];
                idx = (idx + 1) % len;
            }
            for (int i = bottom - 1; i > top; i--) {
                grid[i][left] = temp[idx];
                idx = (idx + 1) % len;
            }
        }
        
        return grid;
    }
}
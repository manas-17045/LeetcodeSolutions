// Leetcode 1260: Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/
// Solved on 20th of July, 2026
class Solution {
    /**
     * Shifts the 2D grid by k positions.
     * @param grid The 2D grid.
     * @param k The number of positions to shift.
     * @return The shifted 2D grid.
     */
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int totalElements = m * n;
        k = k % totalElements;
        List<List<Integer>> shiftedGrid = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            List<Integer> currentRow = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                int newFlatIndex = i * n + j;
                int originalFlatIndex = (newFlatIndex - k + totalElements) % totalElements;
                currentRow.add(grid[originalFlatIndex / n][originalFlatIndex % n]);
            }
            shiftedGrid.add(currentRow);
        }
        return shiftedGrid;
    }
}
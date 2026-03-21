// Leetcode 3643: Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/
// Solved on 21st of March, 2026
class Solution {
    /**
     * Flips a square submatrix of size k x k vertically within the given grid.
     *
     * @param grid The 2D integer array containing the matrix.
     * @param x    The starting row index of the top-left corner of the submatrix.
     * @param y    The starting column index of the top-left corner of the submatrix.
     * @param k    The size of the square submatrix to be flipped.
     * @return The modified grid with the submatrix flipped vertically.
     */
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        for (int i = 0; i < k / 2; i++) {
            for (int j = 0; j < k; j++) {
                int temp = grid[x + i][y + j];
                grid[x + i][y + j] = grid[x + k - 1 - i][y + j];
                grid[x + k - 1 - i][y + j] = temp;
            }
        }
        return grid;
    }
}
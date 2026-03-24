// Leetcode 2906: Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/
// Solved on 24th of March, 2026
class Solution {
    /**
     * Constructs a product matrix where each element at (i, j) is the product of all 
     * elements in the original grid except grid[i][j], modulo 12345.
     * @param grid A 2D integer array of size n x m.
     * @return A 2D integer array p of size n x m representing the product matrix.
     */
    public int[][] constructProductMatrix(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] p = new int[n][m];
        long prefix = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                p[i][j] = (int) prefix;
                prefix = (prefix * grid[i][j]) % 12345;
            }
        }
        
        long suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                p[i][j] = (int) ((p[i][j] * suffix) % 12345);
                suffix = (suffix * grid[i][j]) % 12345;
            }
        }
        
        return p;
    }
}
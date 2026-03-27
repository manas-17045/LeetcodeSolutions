// Leetcode 2946: Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
// Solved on 27th of March, 2026
class Solution {
    /**
     * Checks if the matrix remains the same after cyclic shifts of its rows.
     * Even-indexed rows are shifted left and odd-indexed rows are shifted right.
     * @param mat The m x n integer matrix.
     * @param k The number of times to perform the cyclic shift.
     * @return true if the matrix after shifts is identical to the original, false otherwise.
     */
    public boolean areSimilar(int[][] mat, int k) {
        int rows = mat.length;
        int cols = mat[0].length;
        int shift = k % cols;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (i % 2 == 0) {
                    if (mat[i][j] != mat[i][(j + shift) % cols]) {
                        return false;
                    }
                } else {
                    if (mat[i][j] != mat[i][(j - shift + cols) % cols]) {
                        return false;
                    }
                }
            }
        }
        
        return true;
    }
}
// Leetcode 1582: Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/
// Solved on 4th of March, 2026
class Solution {
    /**
     * Counts the number of special positions in a binary matrix.
     * A position (i, j) is special if mat[i][j] == 1 and all other elements in row i and column j are 0.
     * 
     * @param mat The input binary matrix.
     * @return The number of special positions.
     */
    public int numSpecial(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[] rowSum = new int[rows];
        int[] colSum = new int[cols];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] == 1) {
                    rowSum[i]++;
                    colSum[j]++;
                }
            }
        }
        
        int result = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] == 1 && rowSum[i] == 1 && colSum[j] == 1) {
                    result++;
                }
            }
        }
        
        return result;
    }
}
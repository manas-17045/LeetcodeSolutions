// Leetcode 1886: Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
// Solved on 22nd of March, 2026
class Solution {
    /**
     * Determines if the input matrix can be rotated by 0, 90, 180, or 270 degrees to match the target matrix.
     * 
     * @param mat The n x n source binary matrix.
     * @param target The n x n target binary matrix to compare against.
     * @return true if mat can be rotated to equal target, false otherwise.
     */
    public boolean findRotation(int[][] mat, int[][] target) {
        int n = mat.length;
        boolean rot0 = true;
        boolean rot90 = true;
        boolean rot180 = true;
        boolean rot270 = true;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != target[i][j]) {
                    rot0 = false;
                }
                if (mat[i][j] != target[j][n - 1 - i]) {
                    rot90 = false;
                }
                if (mat[i][j] != target[n - 1 - i][n - 1 - j]) {
                    rot180 = false;
                }
                if (mat[i][j] != target[n - 1 - j][i]) {
                    rot270 = false;
                }
            }
        }
        
        return rot0 || rot90 || rot180 || rot270;
    }
}
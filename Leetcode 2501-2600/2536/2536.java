// Leetcode 2536: Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/
// Solved on 14th of November, 2025
class Solution {
    /**
     * Applies a series of range addition queries to an n x n matrix.
     * @param n The size of the square matrix (n x n).
     * @param queries An array of queries, where each query is [r1, c1, r2, c2] representing a submatrix to increment by one.
     * @return The resulting matrix after applying all queries.
     */
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] diff = new int[n+1][n+1];
        for (int[] q : queries) {
            int r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
            diff[r1][c1] += 1;
            diff[r1][c2 + 1] -= 1;
            diff[r2 + 1][c1] -= 1;
            diff[r2 + 1][c2 + 1] += 1;
        }
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i > 0) {
                    diff[i][j] += diff[i - 1][j];
                }
                if (j > 0) {
                    diff[i][j] += diff[i][j - 1];
                }
                if (i > 0 && j > 0) {
                    diff[i][j] -= diff[i - 1][j - 1];
                }
            }
        }
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = diff[i][j];
            }
        }
        return result;
    }
}
// Leetcode 3988: Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/
// Solved on 9th of August, 2026
class Solution {
    /**
     * Creates a grid with exactly k paths from (0, 0) to (m-1, n-1).
     * @param m The number of rows.
     * @param n The number of columns.
     * @param k The number of paths.
     * @return The grid with exactly k paths.
     */
    public String[] createGrid(int m, int n, int k) {
        int blockRows = 0;
        int blockCols = 0;
        boolean hasPattern3x3 = false;

        if (k == 1) {
            blockRows = 1;
            blockCols = 1;
        } else if (k == 2) {
            if (m < 2 || n < 2) {
                return new String[0];
            }
            blockRows = 2;
            blockCols = 2;
        } else if (k == 3) {
            if (m >= 2 && n >= 3) {
                blockRows = 2;
                blockCols = 3;
            } else if (m >= 3 && n >= 2) {
                blockRows = 3;
                blockCols = 2;
            } else {
                return new String[0];
            }
        } else if (k == 4) {
            if (m >= 3 && n >= 3) {
                blockRows = 3;
                blockCols = 3;
                hasPattern3x3 = true;
            } else if (m >= 2 && n >= 4) {
                blockRows = 2;
                blockCols = 4;
            } else if (m >= 4 && n >= 2) {
                blockRows = 4;
                blockCols = 2;
            } else {
                return new String[0];
            }
        }

        String[] result = new String[m];
        for (int i = 0; i < m; i++) {
            StringBuilder rowBuilder = new StringBuilder();
            for (int j = 0; j < n; j++) {
                boolean inBlock = (i < blockRows && j < blockCols);
                boolean isBlockedInBlock = hasPattern3x3 && ((i == 0 && j == 2) || (i == 2 && j == 0));
                boolean inCorridor = (j == blockCols - 1 && i >= blockRows - 1) || (i == m - 1 && j >= blockCols - 1);

                if ((inBlock && !isBlockedInBlock) || inCorridor) {
                    rowBuilder.append('.');
                } else {
                    rowBuilder.append('#');
                }
            }
            result[i] = rowBuilder.toString();
        }

        return result;
    }
}
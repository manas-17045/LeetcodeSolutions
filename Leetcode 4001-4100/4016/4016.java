// Leetcode 4016: Maximum Area of Two Non-Overlapping Square Submatrices
// https://leetcode.com/problems/maximum-area-of-two-non-overlapping-square-submatrices/
// Solved on 8th of September, 2026
class Solution {
    /**
     * Finds the maximum possible area of each of two non-overlapping
     * square submatrices consisting entirely of usable cells.
     *
     * @param mat the 2D grid where 1 represents a usable cell and 0 represents an unusable cell
     * @return the maximum area of each square, or 0 if two such squares cannot be found
     */
    public int maxArea(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[][] dp = new int[rows][cols];

        for (int r = rows - 1; r >= 0; r--) {
            for (int c = cols - 1; c >= 0; c--) {
                if (mat[r][c] == 1) {
                    if (r == rows - 1 || c == cols - 1) {
                        dp[r][c] = 1;
                    } else {
                        dp[r][c] = 1 + Math.min(dp[r + 1][c + 1], Math.min(dp[r + 1][c], dp[r][c + 1]));
                    }
                }
            }
        }

        int low = 1;
        int high = Math.max(Math.min(rows / 2, cols), Math.min(rows, cols / 2));
        int maxSide = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canFormTwoSquares(dp, rows, cols, mid)) {
                maxSide = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return maxSide * maxSide;
    }

    private boolean canFormTwoSquares(int[][] dp, int rows, int cols, int k) {
        int minRow = Integer.MAX_VALUE;
        int minCol = Integer.MAX_VALUE;
        int maxCol = Integer.MIN_VALUE;

        for (int r = 0; r <= rows - k; r++) {
            for (int c = 0; c <= cols - k; c++) {
                if (dp[r][c] >= k) {
                    if (minRow == Integer.MAX_VALUE) {
                        minRow = r;
                    }
                    if (r - minRow >= k) {
                        return true;
                    }
                    if (c < minCol) {
                        minCol = c;
                    }
                    if (c > maxCol) {
                        maxCol = c;
                    }
                    if (maxCol - minCol >= k) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}
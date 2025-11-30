// Leetcode 3742: Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/
// Solved on 30th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum path score in a grid, given a maximum cost `k`.
     * The score is the sum of values in the path, and the cost is the number of non-zero cells visited.
     * @param grid The input grid of integers.
     * @param k The maximum allowed cost (number of non-zero cells).
     * @return The maximum path score, or -1 if no valid path exists.
     */
    public int maxPathScore(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[n][k + 1];

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        dp[0][0] = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    continue;
                }

                int val = grid[i][j];
                int cost = (val == 0) ? 0 : 1;
                int score = val;

                for (int c = k; c >= 0; c--) {
                    int maxScore = -1;

                    if (c >= cost) {
                        int prevCost = c - cost;
                        
                        if (i > 0 && dp[j][prevCost] != -1) {
                            maxScore = Math.max(maxScore, dp[j][prevCost]);
                        }
                        
                        if (j > 0 && dp[j - 1][prevCost] != -1) {
                            maxScore = Math.max(maxScore, dp[j - 1][prevCost]);
                        }
                    }

                    if (maxScore != -1) {
                        dp[j][c] = maxScore + score;
                    } else {
                        dp[j][c] = -1;
                    }
                }
            }
        }

        int result = -1;
        for (int s : dp[n - 1]) {
            result = Math.max(result, s);
        }
        
        return result;
    }
}
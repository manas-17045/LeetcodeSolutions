// Leetcode 3256: Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/
// Solved on 13th of December, 2025
class Solution {
    /**
     * Calculates the maximum value sum by placing three rooks on a board such that no two rooks share the same column.
     * @param board The input 2D integer array representing the board.
     * @return The maximum possible sum of values under the given constraints.
     */
    public long maximumValueSum(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        long maxVal = Long.MIN_VALUE;
        int[][][] topCells = new int[m][3][2];

        for (int i = 0; i < m; i++) {
            for (int k = 0; k < 3; k++) {
                topCells[i][k][0] = Integer.MIN_VALUE;
                topCells[i][k][1] = -1;
            }
            for (int j = 0; j < n; j++) {
                int val = board[i][j];
                if (val > topCells[i][0][0]) {
                    topCells[i][2][0] = topCells[i][1][0];
                    topCells[i][2][1] = topCells[i][1][1];
                    topCells[i][1][0] = topCells[i][0][0];
                    topCells[i][1][1] = topCells[i][0][1];
                    topCells[i][0][0] = val;
                    topCells[i][0][1] = j;
                } else if (val > topCells[i][1][0]) {
                    topCells[i][2][0] = topCells[i][1][0];
                    topCells[i][2][1] = topCells[i][1][1];
                    topCells[i][1][0] = val;
                    topCells[i][1][1] = j;
                } else if (val > topCells[i][2][0]) {
                    topCells[i][2][0] = val;
                    topCells[i][2][1] = j;
                }
            }
        }

        for (int i = 0; i < m - 2; i++) {
            for (int j = i + 1; j < m - 1; j++) {
                for (int k = j + 1; k < m; k++) {
                    for (int a = 0; a < 3; a++) {
                        for (int b = 0; b < 3; b++) {
                            if (topCells[i][a][1] == topCells[j][b][1]) {
                                continue;
                            }
                            for (int c = 0; c < 3; c++) {
                                if (topCells[i][a][1] == topCells[k][c][1] || topCells[j][b][1] == topCells[k][c][1]) {
                                    continue;
                                }
                                long currentSum = (long) topCells[i][a][0] + topCells[j][b][0] + topCells[k][c][0];
                                if (currentSum > maxVal) {
                                    maxVal = currentSum;
                                }
                            }
                        }
                    }
                }
            }
        }

        return maxVal;
    }
}
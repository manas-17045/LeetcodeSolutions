// Leetcode 3429: Paint House IV
// https://leetcode.com/problems/paint-house-iv/
// Solved on 23rd of November, 2025
class Solution {
    /**
     * Calculates the minimum cost to paint a row of `n` houses with 3 available colors,
     * such that no two adjacent houses have the same color, and houses symmetric to the center also have different colors.
     * @param n The number of houses.
     * @param cost A 2D array where cost[i][j] is the cost to paint house `i` with color `j`.
     * @return The minimum cost to paint all houses according to the rules.
     */
    public long minCost(int n, int[][] cost) {
        long[][] prevDp = new long[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                prevDp[i][j] = -1;
            }
        }

        int halfN = n / 2;
        for (int i = 0; i < halfN; i++) {
            long[][] currDp = new long[3][3];
            for (int r = 0; r < 3; r++) {
                for (int c = 0; c < 3; c++) {
                    currDp[r][c] = -1;
                }
            }

            int leftIdx = i;
            int rightIdx = n - 1 - i;

            for (int c1 = 0; c1 < 3; c1++) {
                for (int c2 = 0; c2 < 3; c2++) {
                    if (c1 == c2) {
                        continue;
                    }

                    long currentCost = cost[leftIdx][c1] + cost[rightIdx][c2];

                    if (i == 0) {
                        currDp[c1][c2] = currentCost;
                    } else {
                        long minPrev = Long.MAX_VALUE;
                        boolean found = false;

                        for (int p1 = 0; p1 < 3; p1++) {
                            if (p1 == c1) continue;
                            for (int p2 = 0; p2 < 3; p2++) {
                                if (p2 == c2) continue;
                                if (prevDp[p1][p2] != -1) {
                                    minPrev = Math.min(minPrev, prevDp[p1][p2]);
                                    found = true;
                                }
                            }
                        }

                        if (found) {
                            currDp[c1][c2] = minPrev + currentCost;
                        }
                    }
                }
            }
            prevDp = currDp;
        }

        long minTotalCost = Long.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (prevDp[i][j] != -1) {
                    minTotalCost = Math.min(minTotalCost, prevDp[i][j]);
                }
            }
        }
        return minTotalCost;
    }
}
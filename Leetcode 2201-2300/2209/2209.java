// Leetcode 2209: Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
// Solved on 11th of December, 2025
class Solution {
    /**
     * Given a binary string `floor` representing tiles, where '0' is black and '1' is white.
     * You are given `numCarpets` carpets of length `carpetLen`.
     * The goal is to cover white tiles with carpets to minimize the number of uncovered white tiles.
     * @param floor The binary string representing the tiles.
     * @param numCarpets The number of carpets available.
     * @param carpetLen The length of each carpet.
     * @return The minimum number of white tiles remaining uncovered.
     */
    public int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
        int n = floor.length();
        int[][] dp = new int[n + 1][numCarpets + 1];

        for (int i = 1; i <= n; i++) {
            int isWhite = (floor.charAt(i - 1) == '1') ? 1 : 0;
            for (int k = 0; k <= numCarpets; k++) {
                int skip = dp[i - 1][k] + isWhite;
                int cover = Integer.MAX_VALUE;

                if (k > 0) {
                    cover = dp[Math.max(0, i - carpetLen)][k - 1];
                }

                dp[i][k] = Math.min(skip, cover);
            }
        }

        return dp[n][numCarpets];
    }
}
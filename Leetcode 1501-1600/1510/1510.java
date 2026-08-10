// Leetcode 1510: Stone Game IV
// https://leetcode.com/problems/stone-game-iv/
// Solved on 10th of August, 2026
class Solution {
    /**
     * Determines if Alice wins the stone game IV.
     * 
     * @param n The initial number of stones.
     * @return True if Alice wins, false otherwise.
     */
    public boolean winnerSquareGame(int n) {
        boolean[] dp = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            for (int k = 1; k * k <= i; k++) {
                if (!dp[i - k * k]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
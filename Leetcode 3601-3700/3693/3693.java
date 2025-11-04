// Leetcode 3693: Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/
// Solved on 4th of November, 2025
class Solution {
    /**
     * Calculates the minimum cost to climb to the top of n stairs.
     * @param n The total number of stairs.
     * @param costs An array where costs[i] is the cost to step on stair i+1.
     * @return The minimum cost to reach the nth stair.
     */
    public int climbStairs(int n, int[] costs) {
        int dp = new int[n + 1];
        dp[0] = 0;

        for (int i = 1;  <= n; i++) {
            int cost1= dp[i - 1] + 1;
            int cost2 = Integer.MAX_VALUE;
            int cost3 = Integer.MAX_VALUE;

            if (i - 2 >= 0) {
                cost2 = dp[i - 2] + 4;
            }
            if (i - 3 >= 0) {
                cost3 = dp[i - 3] + 9;
            }

            dp[i] = costs[i - 1] + Math.min(cost1, Math.min(cost2, cost3));
        }

        return dp[n];
    }
}
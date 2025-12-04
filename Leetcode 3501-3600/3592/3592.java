// Leetcode 3592: Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/
// Solved on 4th of November, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Given an array `numWays` where `numWays[i]` is the number of ways to make amount `i+1`
     * using an unknown set of coins, this function attempts to find the smallest set of coins
     * that would produce the given `numWays` array.
     * @param numWays An array where `numWays[i]` is the number of ways to make amount `i+1`.
     * @return A list of integers representing the coins found, or an empty list if no such set of coins can be determined or if the input is inconsistent.
     */
    public List<Integer> findCoins(int[] numWays) {
        int n = numWays.length;
        long[] dp = new long[n + 1];
        dp[0] = 1;
        List<Integer> coins = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            long currentWays = dp[i];
            long targetWays = numWays[i - 1];

            if (currentWays > targetWays) {
                return new ArrayList<>();
            }

            if (currentWays == targetWays) {
                continue;
            }

            if (targetWays - currentWays != 1) {
                return new ArrayList<>();
            }

            coins.add(i);

            for (int j = i; j <= n; j++) {
                dp[j] += dp[j - i];
            }
        }

        return coins;
    }
}
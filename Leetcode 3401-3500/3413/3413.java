// Leetcode 3413: Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/
// Solved on 31st of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum coins that can be collected from k consecutive bags.
     * @param coins A 2D array where each element `coins[i] = [start_pos, end_pos, coin_value]` represents a bag of coins.
     * @param k The number of consecutive bags to consider.
     * @return The maximum number of coins that can be collected.
     */
    public long maximumCoins(int[][] coins, int k) {
        int n = coins.length;
        Arrays.sort(coins, (a, b) -> Integer.compare(a[0], b[0]));

        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (long)(coins[i][1] - coins[i][0] + 1) * coins[i][2];
        }

        long maxCoins = 0;

        for (int i = 0, j = 0; i < n; i++) {
            long end = (long)coins[i][0] + k - 1;
            while (j < n && coins[j][0] <= end) {
                j++;
            }
            
            long current = prefix[j] - prefix[i];
            
            if (j > 0) {
                long segEnd = coins[j - 1][1];
                if (segEnd > end) {
                    current -= (segEnd - end) * coins[j - 1][2];
                }
            }
            maxCoins = Math.max(maxCoins, current);
        }

        for (int i = 0, j = 0; i < n; i++) {
            long start = (long)coins[i][1] - k + 1;
            while (j < n && coins[j][1] < start) {
                j++;
            }

            if (j <= i) {
                long current = prefix[i + 1] - prefix[j];
                long segStart = coins[j][0];
                if (segStart < start) {
                    current -= (start - segStart) * coins[j][2];
                }
                maxCoins = Math.max(maxCoins, current);
            }
        }

        return maxCoins;
    }
}
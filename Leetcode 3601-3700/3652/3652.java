// Leetcode 3652: Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/
// Solved on 25th of November, 2025
class Solution {
    /**
     * Calculates the maximum profit achievable given stock prices, a buying/selling strategy, and a window size k.
     * @param prices An array of stock prices.
     * @param strategy An array representing the strategy (e.g., 0 for sell, 1 for buy).
     * @param k The window size for strategy adjustment.
     * @return The maximum profit.
     */
    public long maxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.length;
        long baseProfit = 0;
        for (int i = 0; i < n; i++) {
            baseProfit += (long) strategy[i] * prices[i];
        }

        int halfK = k / 2;
        long currentDiff = 0;

        for (int i = 0; i < halfK; i++) {
            currentDiff -= (long) strategy[i] * prices[i];
        }
        for (int i = halfK; i < k; i++) {
            currentDiff += (long) prices[i] * (1 - strategy[i]);
        }

        long maxDiff = Math.max(0, currentDiff);

        for (int i = 0; i < n - k; i++) {
            currentDiff += (long) strategy[i] * prices[i];
            currentDiff -= prices[i + halfK];
            currentDiff += (long) prices[i + k] * (1 - strategy[i + k]);
            maxDiff = Math.max(maxDiff, currentDiff);
        }

        return baseProfit + maxDiff;
    }
}
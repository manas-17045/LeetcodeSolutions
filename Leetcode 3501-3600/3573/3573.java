// Leetcode 3573: Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
// Solved on 17th of December, 2025
class Solution {
    public long maximumProfit(int[] prices, int k) {
        /**
         * Calculates the maximum profit that can be achieved by performing at most k transactions.
         * A transaction involves buying and selling a stock.
         * @param prices An array of stock prices where prices[i] is the price on day i.
         * @param k The maximum number of transactions allowed.
         * @return The maximum profit.
         */
        int n = prices.length;
        long[] closed = new long[k + 1];
        long[] longHold = new long[k + 1];
        long[] shortHold = new long[k + 1];

        // Initialize arrays with a sufficiently small value to represent unreachable states
        for (int i = 1; i <= k; i++) {
            closed[i] = Long.MIN_VALUE / 2;
            longHold[i] = Long.MIN_VALUE / 2;
            shortHold[i] = Long.MIN_VALUE / 2;
        }
        
        closed[0] = 0;
        longHold[0] = Long.MIN_VALUE / 2;
        shortHold[0] = Long.MIN_VALUE / 2;

        for (int price : prices) {
            long[] nextClosed = closed.clone();
            long[] nextLongHold = longHold.clone();
            long[] nextShortHold = shortHold.clone();

            for (int j = 1; j <= k; j++) {
                nextLongHold[j] = Math.max(longHold[j], closed[j - 1] - price);

                nextShortHold[j] = Math.max(shortHold[j], closed[j - 1] + price);

                nextClosed[j] = Math.max(closed[j], 
                    Math.max(longHold[j] + price, shortHold[j] - price));
            }

            closed = nextClosed;
            longHold = nextLongHold;
            shortHold = nextShortHold;
        }

        long maxProfit = 0;
        for (long profit : closed) {
            maxProfit = Math.max(maxProfit, profit);
        }

        return maxProfit;
    }
}
// Leetcode 2110: Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
// Solved on 15th of December, 2025
class Solution {
    /**
     * Calculates the number of smooth descent periods in a stock's price history.
     * @param prices An array of integers representing the stock prices.
     * @return The total number of smooth descent periods.
     */
    public long getDescentPeriods(int[] prices) {
        long totalPeriods = 1;
        long currentLength = 1;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] == prices[i - 1] - 1) {
                currentLength++;
            } else {
                currentLength = 1;
            }
            totalPeriods += currentLength;
        }
        return totalPeriods;
    }
}
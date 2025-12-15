// Leetcode 2110: Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
// Solved on 15th of December, 2025
class Solution {
    /**
     * Calculates the number of smooth descent periods in a given array of stock prices.
     * @param prices An array of integers representing the stock prices.
     * @return The total number of smooth descent periods.
     */
    fun getDescentPeroids(prices: IntArray): Long {
        var total: Long = 0
        var currentRun: Long = 0
        for (i in prices.indices) {
            if (i > 0 && prices[i] == prices[i - 1] - 1) {
                currentRun++
            } else {
                currentRun = 1
            }
            total += currentRun
        }
        return total
    }
}
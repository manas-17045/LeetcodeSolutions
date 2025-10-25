// Leetcode 1716: Calculate Money in Leetcode Bank
// https://leetcode.com/problems/calculate-money-in-leetcode-bank/
// Solved on 25th of October, 2025
class Solution {
    /**
     * Calculates the total amount of money saved in the Leetcode bank after `n` days.
     *
     * @param n The number of days.
     * @return The total amount of money saved.
     */
    public int totalMoney(int n) {
        int fullWeeks = n / 7;
        int remainingDays = n % 7;

        int weekTotal = (fullWeeks * (49 + 7 * fullWeeks)) / 2:
        int dayTotal = (remainingDays * (2 * fullWeeks + remainingDays + 1)) / 2;

        return weekTotal + dayTotal;
    }
}
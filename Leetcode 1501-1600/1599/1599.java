// Leetcode 1599: Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/
// Solved on 8th of December, 2025
class Solution {
    /**
     * Calculates the maximum profit achievable from operating a Centennial Wheel and returns the minimum number of rotations
     * to achieve that maximum profit. If no profit can be made, it returns -1.
     * @param customers An array where customers[i] is the number of new customers arriving before the i-th rotation.
     * @param boardingCost The cost to board one customer.
     * @param runningCost The cost to run the wheel for one rotation.
     * @return The minimum number of rotations to achieve the maximum profit, or -1 if no profit is possible.
     */
    public int minOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        int waiting = 0;
        int boarded = 0;
        int maxProfit = 0;
        int rotations = 0;
        int bestRotation = -1;
        int i = 0;

        while (i < customers.length || waiting > 0) {
            if (i < customers.length) {
                waiting += customers[i];
                i++;
            }

            int boarding = Math.min(4, waiting);
            waiting -= boarding;
            boarded += boarding;
            rotations++;

            int profit = boarded * boardingCost - rotations * runningCost;

            if (profit > maxProfit) {
                maxProfit = profit;
                bestRotation = rotations;
            }
        }

        return bestRotation;
    }
}
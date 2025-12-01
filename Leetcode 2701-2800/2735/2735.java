// Leetcode 2735: Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/
// Solved on 1st of December, 2025
class Solution {
    public long minCost(int[] nums, int x) {
        /**
         * Calculates the minimum cost to collect all chocolates.
         *
         * @param nums An array representing the initial costs of chocolates.
         * @param x The cost to shift all chocolates to the right by one position.
         * @return The minimum total cost to collect all chocolates.
         */
        int n = nums.length;
        long[] minCosts = new long[n];
        for (int i = 0; i < n; i++) {
            minCosts[i] = nums[i];
        }

        long minTotalCost = 0;
        for (long cost : minCosts) {
            minTotalCost += cost;
        }

        for (int k = 1; k < n; k++) {
            long currentCycleCost = 0;
            for (int i = 0; i < n; i++) {
                int shiftedIndex = (i - k + n) % n;
                minCosts[i] = Math.min(minCosts[i], nums[shiftedIndex]);
                currentCycleCost += minCosts[i];
            }
            minTotalCost = Math.min(minTotalCost, currentCycleCost + (long) k * x);
        }

        return minTotalCost;
    }
}
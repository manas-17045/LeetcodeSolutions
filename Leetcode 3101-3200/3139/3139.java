// Leetcode 3139: Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/
// Solved on 12th of December, 2025
class Solution {
    /**
     * Calculates the minimum cost to equalize all elements in an array.
     * @param nums The input array of integers.
     * @param cost1 The cost to increment a single element by 1.
     * @param cost2 The cost to increment two distinct elements by 1.
     * @return The minimum cost to make all elements equal, modulo 1,000,000,007.
     */
    public int minCostToEqualizeArray(int[] nums, int cost1, int cost2) {
        long minVal = Integer.MAX_VALUE;
        long maxVal = Integer.MIN_VALUE;
        long totalSum = 0;
        int n = nums.length;

        for (int num : nums) {
            minVal = Math.min(minVal, num);
            maxVal = Math.max(maxVal, num);
            totalSum += num;
        }

        long totalGap = maxVal * n - totalSum;

        if (cost1 * 2 <= cost2 || n <= 2) {
            return (int) ((totalGap * cost1) % 1_000_000_007);
        }

        long minCost = Long.MAX_VALUE;

        for (long target = maxVal; target <= maxVal + 2; target++) {
            minCost = Math.min(minCost, calculateCost(target, n, totalSum, minVal, cost1, cost2));
        }

        long limit = (totalSum - 2 * minVal) / (n - 2);
        
        if (limit >= maxVal) {
            for (long target = limit - 1; target <= limit + 2; target++) {
                if (target >= maxVal) {
                    minCost = Math.min(minCost, calculateCost(target, n, totalSum, minVal, cost1, cost2));
                }
            }
        }

        return (int) (minCost % 1_000_000_007);
    }

    private long calculateCost(long target, int n, long totalSum, long minVal, int cost1, int cost2) {
        long totalGap = target * n - totalSum;
        long maxGap = target - minVal;
        long otherGaps = totalGap - maxGap;

        if (maxGap > otherGaps) {
            return otherGaps * cost2 + (maxGap - otherGaps) * cost1;
        } else {
            long pairs = totalGap / 2;
            long cost = pairs * cost2;
            if (totalGap % 2 != 0) {
                cost += cost1;
            }
            return cost;
        }
    }
}
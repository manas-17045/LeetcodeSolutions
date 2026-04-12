// Leetcode 3891: Minimum Increase to Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/
// Solved on 12th of April, 2026
class Solution {
    /**
     * Calculates the minimum total increase required to maximize the number of special indices.
     * A special index is defined as an index i where nums[i] > nums[i-1] and nums[i] > nums[i+1].
     * @param nums An array of integers.
     * @return The minimum total increase needed as a long.
     */
    public long minIncrease(int[] nums) {
        int n = nums.length;
        if (n % 2 != 0) {
            long totalCost = 0;
            for (int i = 1; i < n - 1; i += 2) {
                totalCost += getCost(nums, i);
            }
            return totalCost;
        } else {
            int k = (n - 2) / 2;
            long currentSum = 0;
            for (int i = 0; i < k; i++) {
                currentSum += getCost(nums, 2 * i + 2);
            }
            
            long minSum = currentSum;
            for (int i = 0; i < k; i++) {
                currentSum -= getCost(nums, 2 * i + 2);
                currentSum += getCost(nums, 2 * i + 1);
                if (currentSum < minSum) {
                    minSum = currentSum;
                }
            }
            return minSum;
        }
    }

    private long getCost(int[] nums, int index) {
        int maxNeighbor = Math.max(nums[index - 1], nums[index + 1]);
        if (nums[index] <= maxNeighbor) {
            return maxNeighbor + 1L - nums[index];
        }
        return 0;
    }
}
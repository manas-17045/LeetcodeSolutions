// Leetcode 3434: Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/
// Solved on 19th of November, 2025
class Solution {
    /**
     * Calculates the maximum frequency of an element after performing at most one subarray operation.
     * A subarray operation consists of choosing a subarray and changing all its elements to a target value.
     * @param nums An array of integers.
     * @param k The target value for the subarray operation.
     * @return The maximum possible frequency of any element after the operation.
     */
    public int maxFrequency(int[] nums, int k) {
        int originalCount = 0;
        boolean[] present = new boolean[51];

        for (int num : nums) {
            if (num == k) {
                originalCount++;
            }
            present[num] = true;
        }

        int maxGain = 0;

        for (int target = 1; target <= 50; target++) {
            if (target == k || !present[target]) {
                continue;
            }

            int currentSum = 0;
            int maxSubarraySum = 0;

            for (int num : nums) {
                if (num == target) {
                    currentSum++;
                } else if (num == k) {
                    currentSum--;
                }

                if (currentSum < 0) {
                    currentSum = 0;
                }

                maxSubarraySum = Math.max(maxSubarraySum, currentSum);
            }

            maxGain = Math.max(maxGain, maxSubarraySum);
        }

        return originalCount + maxGain;
    }
}
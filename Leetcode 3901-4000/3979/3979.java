// Leetcode 3979: Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/
// Solved on 26th of July, 2026
class Solution {
    /**
     * Finds the maximum sum of any pair (nums[i], nums[j]) such that the conditions are satisfied.
     * @param nums The array of integers.
     * @param k The constraint for the pair sum.
     * @return The maximum valid pair sum.
     */
    public int maxValidPairSum(int[] nums, int k) {
        int maxPrefix = nums[0];
        int maxPairSum = nums[0] + nums[k];
        for (int rightIndex = k; rightIndex < nums.length; rightIndex++) {
            maxPrefix = Math.max(maxPrefix, nums[rightIndex - k]);
            maxPairSum = Math.max(maxPairSum, maxPrefix + nums[rightIndex]);
        }
        return maxPairSum;
    }
}
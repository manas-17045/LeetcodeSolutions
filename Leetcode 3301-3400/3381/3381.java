// Leetcode 3381: Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/
// Solved on 27th of of November, 2025
class Solution {
    public long maxSubarraySum(int[] nums, int k) {
    /**
     * Finds the maximum subarray sum where the length of the subarray is divisible by k.
     *
     * @param nums The input array of integers.
     * @param k The divisor for the subarray length.
     * @return The maximum subarray sum with length divisible by k.
     */
        long maxSum = Long.MIN_VALUE;
        long currentSum = 0;
        long[] minPrefix = new long[k];
        
        for (int i = 0; i < k; i++) {
            minPrefix[i] = Long.MAX_VALUE;
        }
        minPrefix[0] = 0;

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            int remainder = (i + 1) % k;
            
            if (minPrefix[remainder] != Long.MAX_VALUE) {
                maxSum = Math.max(maxSum, currentSum - minPrefix[remainder]);
            }
            
            minPrefix[remainder] = Math.min(minPrefix[remainder], currentSum);
        }
        
        return maxSum;
    }
}
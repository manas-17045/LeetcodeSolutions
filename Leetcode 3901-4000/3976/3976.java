// Leetcode 3976: Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/
// Solved on 19th of July, 2026
class Solution {
    /**
     * Finds the maximum subarray sum after applying at most one multiplier operation.
     * 
     * @param nums The input array.
     * @param k The multiplier.
     * @return The maximum subarray sum.
     */
    public long maxSubarraySum(int[] nums, int k) {
        long dp0 = Long.MIN_VALUE / 2;
        long dp1 = Long.MIN_VALUE / 2;
        long dp2 = Long.MIN_VALUE / 2;
        long dp3 = Long.MIN_VALUE / 2;
        long maxSum = Long.MIN_VALUE;

        for (int num : nums) {
            long mul = (long) num * k;
            long div = (long) num / k;

            long nextDp0 = Math.max((long) num, dp0 + num);
            long nextDp1 = Math.max(mul, Math.max(dp0 + mul, dp1 + mul));
            long nextDp2 = Math.max(div, Math.max(dp0 + div, dp2 + div));
            long nextDp3 = Math.max(dp1 + num, Math.max(dp2 + num, dp3 + num));

            dp0 = nextDp0;
            dp1 = nextDp1;
            dp2 = nextDp2;
            dp3 = nextDp3;

            maxSum = Math.max(maxSum, Math.max(Math.max(dp0, dp1), Math.max(dp2, dp3)));
        }

        return maxSum;
    }
}
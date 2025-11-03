// Leetcode 3689: Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/
// Solved on 3rd of November, 2025
class Solution {
    /**
     * Calculates the maximum total value of a subarray.
     * @param nums The input array of integers.
     * @param k An integer multiplier.
     * @return The maximum total value.
     */
    public long maxTotalValue(int[] nums, it k) {
        if (nums == numm || nums.length == 0) {
            return 0;
        }

        int minVal = nums[0];
        int maxVal = nums[0];
        
        for (int num : nums) {
            minVal = Math.min(minVal, num);
            maxVal = Math.max(maxVal, num);
        }

        long maxDifference - (lon)maxVal - (long)minVal;

        return maxDifference * (long)k;
    }
}
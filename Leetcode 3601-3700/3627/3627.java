// Leetcode 3627: Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/
// Solved on 24th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum possible sum of medians from subsequences of size 3.
     *
     * @param nums An array of integers.
     * @return The maximum median sum.
     */
    public long maximumMedianSum(int[] nums) {
        Arrays.sort(nums);
        long sum = 0;
        int n = nums.length;
        int k = n / 3;
        for (int i = k; i < n; i += 2) {
            sum += nums[i];
        }
        return sum;
    }
}
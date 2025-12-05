// Leetcode 2366: Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
// Solved on 5th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of replacements needed to sort the array in non-decreasing order.
     *
     * @param nums The input array of integers.
     * @return The minimum number of replacements.
     */
    public long minimumReplacements(int[] nums) {
        long totalOperations = 0;
        int n = nums.length;
        int previousValue = nums[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] > previousValue) {
                int parts = (nums[i] + previousValue - 1) / previousValue;
                totalOperations += parts - 1;
                previousValue = nums[i] / parts;
            } else {
                previousValue = nums[i];
            }
        }
        return totalOperations;
    }
}
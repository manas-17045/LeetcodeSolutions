// Leetcode 3818: Minimum Prefix Removal to Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/
// Solved on 28th of January, 2026
class Solution {
    /**
     * Calculates the minimum prefix length to remove to make the array strictly increasing.
     *
     * @param nums The input integer array.
     * @return The minimum length of the prefix to be removed.
     */
    public int minimumPrefixLength(int[] nums) {
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] >= nums[i + 1]) {
                return i + 1;
            }
        }
        return 0;
    }
}
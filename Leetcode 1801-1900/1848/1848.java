// Leetcode 1848: Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/
// Solved on 13th of April, 2026
class Solution {
    /**
     * Finds the minimum distance |i - start| such that nums[i] == target.
     * 
     * @param nums   An integer array.
     * @param target The integer value to search for.
     * @param start  The starting index to calculate distance from.
     * @return       The minimum absolute distance to the target element.
     */
    public int getMinDistance(int[] nums, int target, int start) {
        for (int i = 0; i < nums.length; i++) {
            if (start + i < nums.length && nums[start + i] == target) {
                return i;
            }
            if (start - i >= 0 && nums[start - i] == target) {
                return i;
            }
        }
        return 0;
    }
}
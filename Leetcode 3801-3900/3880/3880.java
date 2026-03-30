// Leetcode 3880: Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/
// Solved on 30th of March, 2026
class Solution {
    /**
     * Calculates the minimum absolute difference between the indices of the values 1 and 2 in the array.
     *
     * @param nums An integer array containing values including 1s and 2s.
     * @return The minimum distance between any 1 and any 2, or -1 if either value is missing.
     */
    public int minAbsoluteDifference(int[] nums) {
        int lastOne = -1;
        int lastTwo = -1;
        int minDiff = Integer.MAX_VALUE;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                lastOne = i;
                if (lastTwo != -1) {
                    minDiff = Math.min(minDiff, i - lastTwo);
                }
            } else if (nums[i] == 2) {
                lastTwo = i;
                if (lastOne != -1) {
                    minDiff = Math.min(minDiff, i - lastOne);
                }
            }
        }
        
        return minDiff == Integer.MAX_VALUE ? -1 : minDiff;
    }
}
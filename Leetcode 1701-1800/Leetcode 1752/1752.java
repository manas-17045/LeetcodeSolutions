// Leetcode 1752: Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
// Solved on 23rd of May, 2026
class Solution {
    /**
     * Checks if the array was originally sorted in non-decreasing order, then rotated some number of positions.
     *
     * @param nums An array of integers.
     * @return True if the array is sorted and rotated, false otherwise.
     */
    public boolean check(int[] nums) {
        int dropCount = 0;
        int arrayLength = nums.length;

        for (int i = 0; i < arrayLength; i++) {
            if (nums[i] > nums[(i + 1) % arrayLength]) {
                dropCount++;
            }
        }

        return dropCount <= 1;
    }
}
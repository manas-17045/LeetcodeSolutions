// Leetcode 3978: Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/
// Solved on 26th of July, 2026
class Solution {
    /**
     * Checks if the middle element of the array is unique.
     * @param nums The array of integers.
     * @return True if the middle element is unique, False otherwise.
     */
    public boolean isMiddleElementUnique(int[] nums) {
        int target = nums[nums.length / 2];
        int count = 0;
        for (int num : nums) {
            if (num == target) {
                count++;
            }
        }
        return count == 1;
    }
}
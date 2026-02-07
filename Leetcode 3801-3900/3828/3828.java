// Leetcode 3828: Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/
// Solved on 7th of February, 2026
class Solution {
    /**
     * Calculates the final element remaining after performing subarray deletions.
     * @param nums An array of integers.
     * @return The maximum value between the first and the last element of the array.
     */
    public int finalElement(int[] nums) {
        int n = nums.length;
        return Math.max(nums[0], nums[n-1]);
    }
}
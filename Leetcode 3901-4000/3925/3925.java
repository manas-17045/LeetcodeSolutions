// Leetcode 3925: Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/
// Solved on 24th of May, 2026
class Solution {
    /**
     * Concatenates the given array with its reverse.
     * @param nums The input integer array.
     * @return A new array containing the original elements followed by the elements in reverse order.
     */
    public int[] concatWithReverse(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[n - i - 1];
        }
        return ans;
    }
}
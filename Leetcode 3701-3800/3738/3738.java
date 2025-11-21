// Leetcode 3738: Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/
// Solved on 21st of November, 2025
class Solution {
    /**
     * Finds the length of the longest non-decreasing subarray after replacing at most one element.
     *
     * @param nums The input array of integers.
     * @return The length of the longest non-decreasing subarray.
     */
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return 1;
        }

        int[] right = new int[n];
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) {
                right[i] = right[i + 1] + 1;
            } else {
                right[i] = 1;
            }
        }

        int ans = 1;
        int left = 0;

        for (int i = 0; i < n; i++) {
            int prevLen = left;
            int nextLen = (i < n - 1) ? right[i + 1] : 0;

            ans = Math.max(ans, prevLen + 1);
            ans = Math.max(ans, 1 + nextLen);

            if (i > 0 && i < n - 1 && nums[i + 1] >= nums[i - 1]) {
                ans = Math.max(ans, prevLen + 1 + nextLen);
            }

            if (i > 0 && nums[i] >= nums[i - 1]) {
                left++;
            } else {
                left = 1;
            }
            ans = Math.max(ans, left);
        }

        return ans;
    }
}
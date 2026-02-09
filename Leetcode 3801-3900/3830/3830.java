// Leetcode 3830: Longest Alterenating Subarray After Removing At most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/
// Solved on 9th of February, 2026
class Solution {
    /**
     * Finds the length of the longest alternating subarray after removing at most one element.
     * @param nums An array of integers.
     * @return The maximum length of an alternating subarray possible.
     */
    public int longestAlternating(int[] nums) {
        int n = nums.length;
        int[] up = new int[n];
        int[] down = new int[n];
        int[] rightUp = new int[n];
        int[] rightDown = new int[n];

        for (int i = 0; i < n; i++) {
            up[i] = 1;
            down[i] = 1;
            rightUp[i] = 1;
            rightDown[i] = 1;
        }

        int maxLen = 1;

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                up[i] = down[i - 1] + 1;
                down[i] = 1;
            } else if (nums[i] < nums[i - 1]) {
                down[i] = up[i - 1] + 1;
                up[i] = 1;
            }
            maxLen = Math.max(maxLen, Math.max(up[i], down[i]));
        }

        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                rightUp[i] = rightDown[i + 1] + 1;
                rightDown[i] = 1;
            } else if (nums[i] > nums[i + 1]) {
                rightDown[i] = rightUp[i + 1] + 1;
                rightUp[i] = 1;
            }
        }

        for (int i = 1; i < n - 1; i++) {
            if (nums[i - 1] < nums[i + 1]) {
                maxLen = Math.max(maxLen, down[i - 1] + rightDown[i + 1]);
            } else if (nums[i - 1] > nums[i + 1]) {
                maxLen = Math.max(maxLen, up[i - 1] + rightUp[i + 1]);
            }
        }

        return maxLen;
    }
}
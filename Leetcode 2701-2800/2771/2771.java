// Leetcode 2771: Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/
// Solved on 7th of January, 2026
class Solution {
    /**
     * Finds the length of the longest non-decreasing subarray that can be formed by picking elements
     * from either nums1 or nums2 at each index.
     * @param nums1 The first input array.
     * @param nums2 The second input array.
     * @return The length of the longest non-decreasing subarray.
     */
    public int maxNonDecreasingLength(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int len1 = 1;
        int len2 = 1;
        int maxLen = 1;

        for (int i = 1; i < n; i++) {
            int nextLen1 = 1;
            int nextLen2 = 1;

            if (nums1[i] >= nums1[i - 1]) {
                nextLen1 = Math.max(nextLen1, len1 + 1);
            }
            if (nums1[i] >= nums2[i - 1]) {
                nextLen1 = Math.max(nextLen1, len2 + 1);
            }

            if (nums2[i] >= nums1[i - 1]) {
                nextLen2 = Math.max(nextLen2, len1 + 1);
            }
            if (nums2[i] >= nums2[i - 1]) {
                nextLen2 = Math.max(nextLen2, len2 + 1);
            }

            len1 = nextLen1;
            len2 = nextLen2;
            maxLen = Math.max(maxLen, Math.max(len1, len2));
        }

        return maxLen;
    }
}
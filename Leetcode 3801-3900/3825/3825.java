// Leetcode 3825: Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/
// Solved on 7th of February, 2026
class Solution {
    /**
     * Finds the length of the longest strictly increasing subsequence where the bitwise AND 
     * of all elements in the subsequence is non-zero.
     *
     * @param nums An array of integers.
     * @return The length of the longest such subsequence.
     */
    public int longestSubsequence(int[] nums) {
        int maxLen = 0;
        int[] tails = new int[nums.length];

        for (int bit = 0; bit < 30; bit++) {
            int size = 0;
            int mask = 1 << bit;
            for (int num : nums) {
                if ((num & mask) != 0) {
                    int low = 0;
                    int high = size;
                    while (low < high) {
                        int mid = (low + high) / 2;
                        if (tails[mid] < num) {
                            low = mid + 1;
                        } else {
                            high = mid;
                        }
                    }
                    if (low == size) {
                        size++;
                    }
                    tails[low] = num;
                }
            }
            if (size > maxLen) {
                maxLen = size;
            }
        }
        return maxLen;
    }
}
// Leetcode 3702: Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
// Solved on 4th of November, 2025
class Solution {
    /**
     * Finds the length of the longest subsequence such that the bitwise XOR sum of its elements is non-zero.
     *
     * @param nums The input array of integers.
     * @return The length of the longest subsequence with a non-zero bitwise XOR sum.
     */
    public int longestSubsequence(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return 0;
        }
        int totalXor = 0;
        int nonZeroCount = 0;
        for (int v : nums) {
            totalXor ^= v;
            if (v != 0) {
                nonZeroCount++;
            }
        }
        if (totalXor != 0) {
            return n;
        }
        if (nonZeroCount > 0) {
            return n - 1;
        }
        return 0;
    }
}
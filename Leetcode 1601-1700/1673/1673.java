// Leetcode 1673: Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/
// Solved on 28th of October, 2025
class Solution {
    /**
     * Finds the most competitive subsequence of length k from the given array nums.
     * @param nums The input array of integers.
     * @param k The desired length of the competitive subsequence.
     * @return An array representing the most competitive subsequence.
     */
    public int[] mostCompetitive(int[] nums, int k) {
        int[] result = new int[k];
        int top = -1;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int currentNum = nums[i];

            while (top >= 0 && currentNum < result[top] && (top + n - i >= k)) {
                top--;
            }

            if (top < k - 1) {
                top++;
                result[top] = currentNum;
            }
        }

        return result;
    }
}
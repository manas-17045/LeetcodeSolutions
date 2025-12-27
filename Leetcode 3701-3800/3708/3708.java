// Leetcode 3708: Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/
// Solved on 27th of December, 2025
class Solution {
    /**
     * Finds the length of the longest Fibonacci-like subarray.
     * @param nums The input array of integers.
     * @return The length of the longest Fibonacci-like subarray.
     */
    public int longestSubarray(int[] nums) {
        int maxLength = 0;
        int currentLength = 2;
        
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + nums[i - 2]) {
                currentLength++;
            } else {
                currentLength = 2;
            }
            maxLength = Math.max(maxLength, currentLength);
        }
        
        return maxLength;
    }
}
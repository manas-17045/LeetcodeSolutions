// Leetcode 1980: Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/
// Solved on 8th of March, 2026
class Solution {
    /**
     * Finds a binary string of length n that does not appear in the given array of n strings.
     * Uses Cantor's Diagonal Argument to construct a unique string.
     *
     * @param nums An array of n binary strings, each of length n.
     * @return A binary string of length n that is not present in nums.
     */
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < nums.length; i++) {
            result.append(nums[i].charAt(i) == '0' ? '1' : '0');
        }
        return result.toString();
    }
}
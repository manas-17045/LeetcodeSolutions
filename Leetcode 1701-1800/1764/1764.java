// Leetcode 1764: Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
// Solved on 10th of November, 2025
class Solution {
    /**
     * Checks if all groups can be found as contiguous subarrays in nums, in their given order.
     * @param groups An array of integer arrays, where each inner array represents a group.
     * @param nums The main array of integers to search within.
     * @return True if all groups can be formed by concatenating subarrays of nums, false otherwise.
     */
    public boolean canChoose(int[][] groups, int[] nums) {
        int pos = 0;
        for (int[] group : groups) {
            if (pos > nums.length - group.length) return false;
            int[] lps = buildLPS(group);
            int j = 0;
            boolean matched = false;
            for (int i = pos; i < nums.length; i++) {
                while (j > 0 && nums[i] != group[j]) j = lps[j - 1];
                if (nums[i] == group[j]) j++;
                if (j == group.length) {
                    pos = i - group.length + 1 + group.length;
                    matched = true;
                    break;
                }
            }
            if (!matched) return false;
        }
        return true;
    }
    private int[] buildLPS(int[] pattern) {
        int n = pattern.length;
        int[] lps = new int[n];
        int len = 0;
        for (int i = 1; i < n; i++) {
            while (len > 0 && pattern[i] != pattern[len]) len = lps[len - 1];
            if (pattern[i] == pattern[len]) len++;
            lps[i] = len;
        }
        return lps;
    }
}
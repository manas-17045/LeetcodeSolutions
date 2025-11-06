// Leetcode 2262: Total Appeal of a String
// https://leetcode.com/problems/total-appeal-of-a-string/
// Solved on 6th of November, 2025
class Solution {
    public long appealSum(String s) {
        /**
         * Calculates the total appeal of a string. The appeal of a substring is the number of distinct characters in it.
         * The total appeal is the sum of the appeals of all substrings.
         * @param s The input string.
         * @return The total appeal of the string.
         */
        int n = s.length();
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) {
            last[i] = -1;
        }
        long result = 0L;
        for (int i = 0; i < n; i++) {
            int idx = s.charAt(i) - 'a';
            long left = i - last[idx];
            long right = n - i;
            result += left * right;
            last[idx] = i;
        }
        return result;
    }
}
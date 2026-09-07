// Leetcode 940: Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/
// Solved on 7th of September, 2026
class Solution {
    /**
     * Calculates the total number of distinct non-empty subsequences
     * that can be formed from the input string.
     *
     * @param s the string consisting of lowercase English letters
     * @return the count of distinct non-empty subsequences modulo 1,000,000,007
     */
    public int distinctSubseqII(String s) {
        int mod = 1_000_000_007;
        int totalCount = 0;
        int[] endCounts = new int[26];

        for (int i = 0; i < s.length(); i++) {
            int charIndex = s.charAt(i) - 'a';
            int newCount = (totalCount + 1) % mod;
            totalCount = (int) (((long) totalCount + newCount - endCounts[charIndex] + mod) % mod);
            endCounts[charIndex] = newCount;
        }

        return totalCount;
    }
}
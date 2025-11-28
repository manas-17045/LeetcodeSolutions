// Leetcode 3039: Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/
// Solved on 28th of November, 2025
class Solution {
    /**
     * Given a string s, apply operations to make the string empty.
     * An operation consists of removing all occurrences of the character that appears the least number of times.
     * @param s The input string.
     * @return The last non-empty string after applying the operations.
     */
    public String lastNonEmptyString(String s) {
        int[] freq = new int[26];
        int maxFreq = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            freq[c - 'a']++;
            maxFreq = Math.max(maxFreq, freq[c - 'a']);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (freq[c - 'a'] == maxFreq) {
                sb.append(c);
                freq[c - 'a']--;
            }
        }

        return sb.reverse().toString();
    }
}
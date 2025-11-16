// Leetcode 1759: Count Number of Homogeneous Substrings
// https://leetcode.com/problems/count-number-of-homogeneous-substrings/
// Solved on 16th of November, 2025
class Solution {
    /**
     * Counts the number of homogeneous substrings in a given string.
     * @param s The input string.
     * @return The number of homogeneous substrings, modulo 10^9 + 7.
     */
    public int countHomogeneous(String s) {
        long mod = 1000000007L;
        long res = 0;
        long runLen = 0;
        char prev = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (i > 0 && c == prev) {
                runLen++;
            } else {
                runLen = 1;
            }
            prev = c;
            res += runLen;
            if (res >= mod) {
                res %= mod;
            }
        }
        return (int)(res % mod);
    }
}
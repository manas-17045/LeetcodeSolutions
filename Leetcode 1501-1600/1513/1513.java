// Leetcode 1513: Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/
// Solved on 16th of November, 2025
class Solution {
    /**
     * Given a binary string s, return the number of substrings with all 1s.
     * @param s The input binary string.
     * @return The number of substrings with all 1s, modulo 10^9 + 7.
     */
    public int numSub(String s) {
        final int mod = 1000000007;
        long res = 0;
        long count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                count++;
                res += count;
                if (res >= mod) {
                    res %= mod;
                }
            } else {
                count = 0;
            }
        }
        return (int)(res % mod);
    }
}
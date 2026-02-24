// Leetcode 3849: Maximum Bitwise XOR After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/
// Solved on 24th of February, 2026
class Solution {
    /**
     * Rearranges the bits of string t to maximize the bitwise XOR with string s.
     * @param s The fixed binary string.
     * @param t The binary string whose bits can be rearranged.
     * @return The resulting binary string after XORing s with the optimally rearranged t.
     */
    public String maximumXor(String s, String t) {
        int n = s.length();
        int ones = 0;
        for (int i = 0; i < n; i++) {
            if (t.charAt(i) == '1') {
                ones++;
            }
        }
        int zeros = n - ones;
        char[] result = new char[n];
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                if (zeros > 0) {
                    result[i] = '1';
                    zeros--;
                } else {
                    result[i] = '0';
                    ones--;
                }
            } else {
                if (ones > 0) {
                    result[i] = '1';
                    ones--;
                } else {
                    results[i] = '0';
                    zeros--;
                }
            }
        }
        return new String(result);
    }
}
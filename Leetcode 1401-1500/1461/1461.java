// Leetcode 1461: Check If a String Contains All Binary Codes of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
// Solved on 18th of November, 2025
class Solution {
    /**
     * Checks if all binary codes of length k are present as substrings in the given string s.
     * @param s The input binary string.
     * @param k The length of the binary codes to check for.
     * @return True if all 2^k binary codes of length k are present in s, false otherwise.
     */
    public boolean hasAllCodes(String s, int k) {
        int n = s.length();
        if (k > n) {
            return false;
        }
        int needed = 1 << k;
        boolean[] seen = new boolean[needed];
        int mask = needed - 1;
        int value = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            value = ((value << 1) & mask) | (s.charAt(i) - '0');
            if (i >= k - 1) {
                if (!seen[value]) {
                    seen[value] = true;
                    count++;
                    if (count == needed) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
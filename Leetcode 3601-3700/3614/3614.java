// Leetcode 3614: Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/
// Solved on 19th of December, 2025
class Solution {
    /**
     * Processes a string with special operations and returns the character at a specific index k.
     *
     * @param s The input string containing characters and special operation symbols.
     * @param k The 0-indexed position of the character to retrieve after all operations.
     * @return The character at position k after processing, or '.' if k is out of bounds.
     */
    public char processStr(String s, long k) {
        int n = s.length();
        long[] lengths = new long[n];
        long currentLength = 0;

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                currentLength++;
            } else if (c == '*') {
                if (currentLength > 0) {
                    currentLength--;
                }
            } else if (c == '#') {
                currentLength *= 2;
            }
            lengths[i] = currentLength;
        }

        if (k >= lengths[n - 1]) {
            return '.';
        }

        for (int i = n - 1; i >= 0; i--) {
            char c = s.charAt(i);
            long len = lengths[i];

            if (c >= 'a' && c <= 'z') {
                if (k == len - 1) {
                    return c;
                }
            } else if (c == '#') {
                long prevLen = len / 2;
                if (k >= prevLen) {
                    k -= prevLen;
                }
            } else if (c == '%') {
                k = len - 1 - k;
            }
        }

        return '.';
    }
}
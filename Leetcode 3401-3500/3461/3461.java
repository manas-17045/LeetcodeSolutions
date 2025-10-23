// Leetcode 3461: Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
// Solved on 23rd of October, 2025
class Solution {
    /**
     * Checks if, after repeatedly applying an operation, the final two digits of a string are the same.
     * The operation involves replacing consecutive pairs of digits with their sum modulo 10.
     * @param s The input string consisting of digits.
     * @return True if the final two digits are the same, false otherwise.
     */
    public boolean hasSameDigits(String s) {
        // Keep performing operations until we have exactly 2 digits
        while (s.length() > 2) {
            StringBuilder next = new StringBuilder();

            // Process consecutive pairs
            for (int i = 0; i < s.length() - 1; i++) {
                int digit1 = s.charAt(i) - '0';
                int digit2 = s.charAt(i + 1) - '0';
                int sum = (digit1 + digit2) % 10;
                next.append(sum);
            }

            s = next.toString();
        }

        // CHeck if the final two sigits are the same
        return s.charAt(0) == s.charAt(1);
    }
}
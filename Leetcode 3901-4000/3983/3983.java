// Leetcode 3983: Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/
// Solved on 1st of August, 2026
class Solution {
    /**
     * Checks if string t can be obtained from string s by deleting zero or more
     * characters from s and then replacing at most one character in the resulting
     * string with any other character.
     *
     * @param s The first string.
     * @param t The second string.
     * @return True if t can be obtained from s by deleting zero or more
     *         characters from s and then replacing at most one character in the
     *         resulting string with any other character, False otherwise.
     */
    public boolean canMakeSubsequence(String s, String t) {
        int sLength = s.length();
        int tLength = t.length();

        if (sLength > tLength) {
            return false;
        }

        if (sLength == 1) {
            return true;
        }

        int[] left = new int[sLength];
        int tIndex = 0;
        for (int i = 0; i < sLength; i++) {
            while (tIndex < tLength && t.charAt(tIndex) != s.charAt(i)) {
                tIndex++;
            }
            if (tIndex < tLength) {
                left[i] = tIndex;
                tIndex++;
            } else {
                left[i] = tLength;
            }
        }

        if (left[sLength - 1] < tLength) {
            return true;
        }

        int[] right = new int[sLength];
        tIndex = tLength - 1;
        for (int i = sLength - 1; i >= 0; i--) {
            while (tIndex >= 0 && t.charAt(tIndex) != s.charAt(i)) {
                tIndex--;
            }
            if (tIndex >= 0) {
                right[i] = tIndex;
                tIndex--;
            } else {
                right[i] = -1;
            }
        }

        for (int i = 0; i < sLength; i++) {
            int leftPos = (i == 0) ? -1 : left[i - 1];
            int rightPos = (i == sLength - 1) ? tLength : right[i + 1];

            if (leftPos < tLength && rightPos >= 0 && rightPos - leftPos >= 2) {
                return true;
            }
        }

        return false;
    }
}
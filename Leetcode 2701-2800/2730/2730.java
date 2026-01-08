// Leetcode 2730: Find the Longest Semi-Repitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/
// Solved on 8th of January, 2026
class Solution {
    /**
     * Finds the length of the longest semi-repetitive substring.
     * A semi-repetitive substring is one that contains at most one pair of adjacent identical characters.
     * @param s The input string.
     * @return The length of the longest semi-repetitive substring.
     */
    public int longestSemiRepetitiveSubstring(String s) {
        int maxLength = 1;
        int currentDuplicateCount = 0;
        int left = 0;

        for (int right = 1; right < s.length(); right++) {
            if (s.charAt(right) == s.charAt(right - 1)) {
                currentDuplicateCount++;
            }

            while (currentDuplicateCount > 1) {
                if (s.charAt(left) == s.charAt(left + 1)) {
                    currentDuplicateCount--;
                }
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
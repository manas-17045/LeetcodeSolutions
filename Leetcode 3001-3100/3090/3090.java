// Leetcode 3090: Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
// Solved on 14th of August, 2026
class Solution {
    /**
     * Computes the maximum length of a substring of s that contains at most two occurrences of each character.
     * 
     * @param s The input string.
     * @return The maximum length of the substring.
     */
    public int maximumLengthSubstring(String s) {
        int[] charCount = new int[26];
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);
            charCount[rightChar - 'a']++;

            while (charCount[rightChar - 'a'] > 2) {
                char leftChar = s.charAt(left);
                charCount[leftChar - 'a']--;
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
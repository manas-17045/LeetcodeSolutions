// Leetcode 3517: Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
// Solved on 31st of December, 2025
class Solution {
    /**
     * Given a string s, rearrange its characters to form the lexicographically smallest palindrome.
     * @param s The input string.
     * @return The lexicographically smallest palindromic rearrangement of s.
     */
    public String smallestPalindrome(String s) {
        int[] charCounts = new int[26];
        int length = s.length();
        for (int i = 0; i < length; i++) {
            charCounts[s.charAt(i) - 'a']++;
        }

        StringBuilder halfBuilder = new StringBuilder();
        String middleChar = "";

        for (int i = 0; i < 26; i++) {
            if (charCounts[i] % 2 != 0) {
                middleChar = String.valueOf((char) (i + 'a'));
            }
            for (int j = 0; j < charCounts[i] / 2; j++) {
                halfBuilder.append((char) (i + 'a'));
            }
        }

        String firstHalf = halfBuilder.toString();
        return firstHalf + middleChar + halfBuilder.reverse().toString();
    }
}
// Leetcode 2472: Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
// Solved on 15th of September, 2026
class Solution {
    /**
     * Calculates the maximum number of non-overlapping palindrome substrings
     * of length at least k that can be selected from a given string.
     *
     * @param s the input string consisting of lowercase English letters
     * @param k the minimum length of each palindrome substring
     * @return the maximum number of valid non-overlapping palindrome substrings
     */
    public int maxPalindrome(String s, int k) {
        int stringLength = s.length();
        int palindromeCount = 0;
        int nextStartIndex = 0;
        
        for (int i = 0; i < stringLength; i++) {
            if (i - k + 1 >= nextStartIndex && isPalindrome(s, i - k + 1, i)) {
                palindromeCount++;
                nextStartIndex = i + 1;
            } else if (i - k >= nextStartIndex && isPalindrome(s, i - k, i)) {
                palindromeCount++;
                nextStartIndex = i + 1;
            }
        }
        
        return palindromeCount;
    }
    
    private boolean isPalindrome(String s, int leftIndex, int rightIndex) {
        while (leftIndex < rightIndex) {
            if (s.charAt(leftIndex) != s.charAt(rightIndex)) {
                return false;
            }
            leftIndex++;
            rightIndex--;
        }
        return true;
    }
}
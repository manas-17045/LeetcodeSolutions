# Leetcode 1930: Unique Length-3 Palindromic Subsequences
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
# Solved on 21st of November, 2025
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Counts the number of unique length-3 palindromic subsequences in the given string `s`.

        Args:
            s (str): The input string.
        Returns:
            int: The number of unique length-3 palindromic subsequences.
        """
        count = 0
        distinctChars = set(s)

        for char in distinctChars:
            first = s.find(char)
            last = s.rfind(char)

            if last > first + 1:
                uniqueMiddleChars = set(s[first + 1: last])
                count += len(uniqueMiddleChars)

        return count
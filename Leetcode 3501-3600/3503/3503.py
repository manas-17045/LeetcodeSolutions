# Leetcode 3503: Longest palindrome After Substring Concatenation I
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/
# Solved on 31st of December, 2025
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        """
        Finds the length of the longest palindrome that can be formed by concatenating a substring from s and a substring from t.

        Args:
            s (str): The first input string.
            t (str): The second input string.
        Returns:
            int: The length of the longest palindrome.
        """
        n = len(s)
        m = len(t)
        maxLen = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if len(sub) > maxLen and sub == sub[::-1]:
                    maxLen = len(sub)

        for i in range(m):
            for j in range(i + 1, m + 1):
                sub = t[i:j]
                if len(sub) > maxLen and sub == sub[::-1]:
                    maxLen = len(sub)

        for i in range(n):
            for j in range(i + 1, n + 1):
                subS = s[i:j]
                lenS = j - i
                for k in range(m):
                    for l in range(k + 1, m + 1):
                        lenT = l - k
                        if lenS + lenT > maxLen:
                            combined = subS + t[k:l]
                            if combined == combined[::-1]:
                                maxLen = lenS + lenT

        return maxLen
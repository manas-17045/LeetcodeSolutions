# Leetcode 3844: Longest Almost-Palindromic Substring
# https://leetcode.com/problems/longest-almost-palindromic-substring/
# Solved on 18th of February, 2026
class Solution:
    def almostPalindromic(self, s: str) -> int:
        """
        Finds the length of the longest almost-palindromic substring.
        An almost-palindromic substring is a string that can become a palindrome by removing at most one character.

        :param s: The input string to search within.
        :return: The length of the longest almost-palindromic substring found.
        """
        n = len(s)
        ans = 0

        for i in range(2 * n - 1):
            l = i // 2
            r = l + (i % 2)

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            baseLen = r - l - 1
            ans = max(ans, baseLen)

            if l < 0 or r >= n:
                if l >= 0 or r < n:
                    ans = max(ans, baseLen + 1)
            else:
                l1, r1 = l - 1, r
                while l1 >= 0 and r1 < n and s[l1] == s[r1]:
                    l1 -= 1
                    r1 += 1
                ans = max(ans, baseLen + 1 + (r1 - r) * 2)

                l2, r2 = l, r + 1
                while l2 >= 0 and r2 < n and s[l2] == s[r2]:
                    l2 -= 1
                    r2 += 1
                ans = max(ans, baseLen + 1 + (l - l2) * 2)

        return ans
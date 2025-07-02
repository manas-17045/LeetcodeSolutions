# Leetcode 1312: Minimum Insertion Steps to Make a String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# Solved on 2nd of July, 2025
class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Calculates the minimum number of insertions required to make a string a palindrome.

        This problem is equivalent to finding the longest palindromic subsequence (LPS)
        of the given string. If the length of the string is `n` and the length of its
        LPS is `lps_len`, then the minimum number of insertions needed is `n - lps_len`.

        Args:
            s: The input string.
        """
        strLength = len(s)
        dp = [0] * strLength

        for i in range((strLength - 1), -1, -1):
            prevVal = 0
            dp[i] = 1

            for j in range((i + 1), strLength):
                tempVal = dp[j]

                if s[i] == s[j]:
                    dp[j] = prevVal + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                prevVal = tempVal

        lpsLength = dp[strLength - 1]

        return strLength - lpsLength
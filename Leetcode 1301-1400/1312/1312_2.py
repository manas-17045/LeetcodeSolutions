# Leetcode 1312: Minimum Insertion Steps to Make a String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# Solved on 2nd of July, 2025
class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Calculates the minimum number of insertions required to make a string a palindrome.
        This is equivalent to n - LPS(s), where LPS(s) is the length of the longest palindromic subsequence of s.
        The LPS is found by calculating the Longest Common Subsequence (LCS) of s and its reverse.

        Args:
            s: The input string.
        """
        n = len(s)
        # t is the reverse of s
        t = s[::-1]

        # dp[j] will hold the length of LCS os s[:i] and t[:j] for the current i
        dp = [0] * (n + 1)

        # Iterate over s (as rows)
        for i in range(1, n + 1):
            # This holds dp[j - 1] from the previous row (i - 1)
            prev = 0
            for j in range(1, (n + 1)):
                # temp will be the old dp[j], i.e. dp[i - 1][j]
                temp = dp[j]
                if s[i - 1] == t[j - 1]:
                    # Match: extend the previous best by 1
                    dp[j] = prev + 1
                else:
                    # Mismatch: Take the max of left (dp[j - 1]) or top (old dp[j])
                    if dp[j - 1] > dp[j]:
                        dp[j] = dp[j - 1]
                # Shift for the next cell: new prev = old dp[j]
                prev = temp

        # dp[n] is now LPS(S); need (n - LPS) insertions
        return n - dp[n]
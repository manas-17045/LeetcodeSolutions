# Leetcode 3472: Longest Palindromic Subsequence After at Most K Operations
# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/
# Solved on 15th of September, 2025
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        """
        Finds the length of the longest palindromic subsequence after at most k operations.

        Args:
            s (str): The input string.
            k (int): The maximum number of operations allowed.

        Returns:
            int: The length of the longest palindromic subsequence.
        """

        n = len(s)
        memo = {}

        def getCost(c1, c2):
            diff = abs(ord(c1) - ord(c2))
            return min(diff, (26 - diff))

        def doSolve(left, right, kRemaining):
            if left > right:
                return 0

            if left == right:
                return 1

            state = (left. right, kRemaining)
            if state in memo:
                return memo[state]

            res = max(doSolve(left + 1, right, kRemaining), doSolve(left, right - 1, kRemaining))

            cost = getCost(s[left], s[right])

            if kRemaining >= cost:
                res = max(res, 2 + doSolve(left + 1, right - 1, kRemaining - cost))

            memo[state] = res
            return res

        return doSolve(0, n - 1, k)
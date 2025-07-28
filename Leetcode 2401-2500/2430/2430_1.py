# Leetcode 2430: Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/
# Solved on 28th of July, 2025
class Solution:
    def deleteString(self, s: str) -> int:
        """
        Calculates the maximum number of operations to delete a string.
        An operation consists of deleting the longest prefix of the string that also appears as a substring starting at a later index.

        Args:
            s (str): The input string.
        Returns:
            int: The maximum number of operations.
        """

        n = len(s)

        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    lcp[i][j] = 1 + lcp[i + 1][j + 1]

        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            prefixLengthLimit = (n - i) // 2
            for j in range(1, prefixLengthLimit + 1):
                if lcp[i][i + j] >= j:
                    dp[i] = max(dp[i], 1 + dp[i + j])

        return dp[0]
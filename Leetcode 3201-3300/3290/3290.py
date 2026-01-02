# Leetcode 3290: Maximum Multiplication Score
# https://leetcode.com/problems/maximum-multiplication-score/
# Solved on 2nd of January, 2025
class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        """
        Calculates the maximum multiplication score.

        Args:
            a: A list of four integers.
            b: A list of integers.
        Returns:
            The maximum multiplication score.
        """

        dp = [-10 ** 18] * 4
        for val in b:
            dp[3] = max(dp[3], dp[2] + val * a[3])
            dp[2] = max(dp[2], dp[1] + val * a[2])
            dp[1] = max(dp[1], dp[0] + val * a[1])
            dp[0] = max(dp[0], val * a[0])

        return dp[3]
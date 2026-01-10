# Leetcode 712: Minimum ASCII Delete Sum for Two Strings
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# Solved on 10th of January, 2026
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Calculates the minimum ASCII sum of deleted characters to make two strings equal.

        Args:
            s1 (str): The first string.
            s2 (str): The second string.
        Returns:
            int: The minimum ASCII sum of deleted characters.
        """
        n = len(s2)
        dp = [0] * (n + 1)

        for c1 in s1:
            prev = 0
            for j, c2 in enumerate(s2):
                temp = dp[j + 1]
                if c1 == c2:
                    dp[j + 1] = prev + ord(c1)
                else:
                    dp[j + 1] = max(dp[j + 1], dp[j])
                prev = temp

        totalAscii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return totalAscii - 2 * dp[n]
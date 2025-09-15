# Leetcode 2712: Minimum Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/
# Solved on 15th of September, 2025
class Solution:
    def minimumCost(self, s: str) -> int:
        """
        Calculates the minimum cost to make all characters in a binary string equal.

        Args:
            s: A binary string consisting of '0's and '1's.
        Returns:
            The minimum cost to make all characters in the string equal.
        """
        n = len(s)
        totalCost = 0
        for i in range(1, n):
            if s[i] != s[i - 1]:
                totalCost += min(i, n - i)

        return totalCost
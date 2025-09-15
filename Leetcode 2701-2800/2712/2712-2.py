# Leetcode 2712: Minimum Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/
# Solved on 15th of September, 2025
class Solution:
    def minimumCost(self, s: str) -> int:
        """
        Calculates the minimum cost to make all characters in the string 's' the same.

        Args:
            s (str): The input string consisting of '0's and '1's.
        Returns:
            int: The minimum cost to make all characters in the string the same.
        """
        n = len(s)
        ans = 0

        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans += min(i, n - i)

        return ans
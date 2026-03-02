# Leetcode 3857: Minimum Cost to Split into Ones
# https://leetcode.com/problems/minimum-cost-to-split-into-ones/
# Solved on 2nd of March, 2026
class Solution:
    def minCost(self, n: int) -> int:
        """
        Calculates the minimum cost to split a number n into ones.

        :param n: The integer to be split.
        :return: The total minimum cost as an integer.
        """
        totalCost = (n * (n - 1)) // 2
        return totalCost
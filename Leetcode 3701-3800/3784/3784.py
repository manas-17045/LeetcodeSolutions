# Leetcode 3784: Minimum Deletion Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/
# Solved on 24th of December, 2025
class Solution:
    def minCost(self, s: str, cost: list[int]) -> int:
        """
        Calculates the minimum cost to delete characters such that all remaining characters are equal.

        Args:
            s (str): The input string.
            cost (list[int]): A list of costs associated with deleting each character.

        Returns:
            int: The minimum deletion cost.
        """
        totalSum = sum(cost)
        charCosts = {}
        maxKeptCost = 0

        for char, value in zip(s, cost):
            currentCost = charCosts.get(char, 0) + value
            charCosts[char] = currentCost
            if currentCost > maxKeptCost:
                maxKeptCost = currentCost

        return totalSum - maxKeptCost
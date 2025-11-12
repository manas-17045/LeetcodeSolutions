# Leetcode 2952: Minimum Number of Coins to be Added
# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/
# Solved on 12th of November, 2025
class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        """
        Calculates the minimum number of coins to add to the given set of coins
        to be able to form any sum from 1 up to the target.

        Args:
            coins (list[int]): A list of integers representing the available coins.
            target (int): The maximum sum that needs to be reachable.

        Returns:
            int: The minimum number of coins that need to be added.
        """
        coins.sort()

        coinsAdded = 0
        reachable = 0
        coinIndex = 0

        while reachable < target:
            nextNeeded = reachable + 1

            if coinIndex < len(coins) and coins[coinIndex] <= nextNeeded:
                reachable += coins[coinIndex]
                coinIndex += 1
            else:
                reachable += nextNeeded
                coinsAdded += 1

        return coinsAdded
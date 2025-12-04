# Leetcode 3592: Inverse Coin Change
# https://leetcode.com/problems/inverse-coin-change/
# Solved on 4th of November, 2025
class Solution:
    def findCoins(self, numWays: list[int]) -> list[int]:
        """
        Finds the set of coins that can produce the given number of ways to make change for each amount.

        Args:
            numWays: A list where numWays[i] is the number of ways to make change for amount i+1.
        Returns:
            A list of integers representing the coins found, or an empty list if no such set of coins exists.
        """
        n = len(numWays)
        currentWays = [0] * (n + 1)
        currentWays[0] = 1
        coins = []

        for i in range(n):
            amount = i + 1
            targetWays = numWays[i]
            current = currentWays[amount]

            diff = targetWays - current

            if diff < 0 or diff > 1:
                return []

            if diff == 1:
                coins.append(amount)
                for j in range(amount, n + 1):
                    currentWays[j] += currentWays[j - amount]

        return coins
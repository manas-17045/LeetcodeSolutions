# Leetcode 1518: Water Bottles
# https://leetcode.com/problems/water-bottles/
# Solved on 1st of October, 2025
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Calculates the maximum number of water bottles you can drink.

        Args:
            numBottles (int): The initial number of full water bottles.
            numExchange (int): The number of empty bottles required to exchange for one full water bottle.

        Returns:
            int: The total number of water bottles drunk.
        """
        totalDrunk = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            newFullBottles = emptyBottles // numExchange
            bottlesLeftOver = emptyBottles % numExchange
            totalDrunk += newFullBottles
            emptyBottles = newFullBottles + bottlesLeftOver

        return totalDrunk
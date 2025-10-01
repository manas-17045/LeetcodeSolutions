# Leetcode 3100: Water Bottles II
# https://leetcode.com/problems/water-bottles-ii/
# Solved on 1st of October, 2025
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """
        Calculates the maximum number of water bottles that can be drunk.

        :param numBottles: The initial number of full water bottles.
        :param numExchange: The initial number of empty bottles required to exchange for one full bottle.
        :return: The total number of bottles drunk.
        """
        bottlesDrunk = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            bottlesDrunk += 1
            emptyBottles += 1
            numExchange += 1

        return bottlesDrunk
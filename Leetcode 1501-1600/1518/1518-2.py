# Leetcode 1518: Water Bottles
# https://leetcode.com/problems/water-bottles/
# Solved on 1st of October, 2025
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Calculates the maximum number of water bottles you can drink.
        :param numBottles: The initial number of full water bottles.
        :param numExchange: The number of empty bottles required to exchange for one full water bottle.
        :return: The total number of water bottles drunk.
        """
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottles = empty // numExchange
            total += new_bottles
            empty = empty % numExchange + new_bottles

        return total
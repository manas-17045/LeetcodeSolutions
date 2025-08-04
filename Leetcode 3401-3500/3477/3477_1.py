# Leetcode 3477: Fruits Into Baskets II
# https://leetcode.com/problems/fruits-into-baskets-ii/
# Solved on 4th of August, 2025
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        """
        Calculates the number of fruits that cannot be placed into any basket.

        Args:
            fruits (list[int]): A list of integers representing the size of each fruit.
            baskets (list[int]): A list of integers representing the capacity of each basket.

        Returns:
            int: The total count of fruits that could not be placed.
        """
        numBaskets = len(baskets)
        basketsUsed = [False] * numBaskets
        unplacedFruitsCount = 0

        for currentFruit in fruits:
            fruitWasPlaced = False
            for i in range(numBaskets):
                if not basketsUsed[i] and baskets[i] >= currentFruit:
                    basketsUsed[i] = True
                    fruitWasPlaced = True
                    break

            if not fruitWasPlaced:
                unplacedFruitsCount += 1

        return unplacedFruitsCount
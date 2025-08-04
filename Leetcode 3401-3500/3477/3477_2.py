# Leetcode 3477: Fruits Into Baskets II
# https://leetcode.com/problems/fruits-into-baskets-ii/
# Solved on 4th of August, 2025
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        """
        Calculates the number of fruits that cannot be placed into any basket.
        :param fruits: A list of integers representing the quantities of fruits.
        :param baskets: A list of integers representing the capacities of the baskets.
        :return: The number of unplaced fruits.
        """
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for qty in fruits:
            # Try o place this fruit in the leftmost valid basket
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= qty:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced
# Leetcode 3861: Minimum Capacity Box
# https://leetcode.com/problems/minimum-capacity-box/
# Solved on 8th of March, 2026
class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        """
        Finds the index of the box with the smallest capacity that can fit the item.

        :param capacity: A list of integers representing the capacity of each box.
        :param itemSize: An integer representing the size of the item to be placed.
        :return: The index of the box with the minimum sufficient capacity, or -1 if no box fits.
        """
        bestIndex = -1
        minCapacity = float('inf')

        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < minCapacity:
                minCapacity = capacity[i]
                bestIndex = i

        return bestIndex
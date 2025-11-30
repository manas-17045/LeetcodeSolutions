# Leetcode 2279: Maximum Bags With Full Capacity of Rocks
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
# Solved on 30th of November, 2025
class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        """
        Calculates the maximum number of bags that can be filled to full capacity.

        Args:
            capacity (list[int]): A list of integers representing the capacity of each bag.
            rocks (list[int]): A list of integers representing the number of rocks currently in each bag.
            additionalRocks (int): An integer representing the number of additional rocks available.

        Returns:
            int: The maximum number of bags that can be filled to full capacity.
        """
        remainingCapacity = []
        for i in range(len(capacity)):
            remainingCapacity.append(capacity[i] - rocks[i])

        remainingCapacity.sort()

        fullBags = 0
        for needed in remainingCapacity:
            if additionalRocks >= needed:
                additionalRocks -= needed
                fullBags += 1
            else:
                break

        return fullBags
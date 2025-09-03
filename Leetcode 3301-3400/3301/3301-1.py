# Leetcode 3301: Maximize the Total Height of Unique Towers
# https://leetcode.com/problems/maximize-the-total-height-of-the-unique-towers/
# Solved on 3rd of September, 2025
class Solution:
    def maximumTotalSum(self, maximumHeight: list[int]) -> int:
        """
        Calculates the maximum possible total height of unique towers.

        Args:
            maximumHeight (list[int]): A list of integers representing the maximum allowed height for each tower.
        Returns:
            int: The maximum total sum of heights of unique towers, or -1 if it's not possible to assign heights.
        """
        maximumHeight.sort(reverse=True)

        totalSum = 0
        availableHeight = float('inf')

        for currentMaxHeight in maximumHeight:
            assignableHeight = min(currentMaxHeight, (availableHeight - 1))

            if assignableHeight < 1:
                return -1

            totalSum += assignableHeight
            availableHeight = assignableHeight

        return totalSum
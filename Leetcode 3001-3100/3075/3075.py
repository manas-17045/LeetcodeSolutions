# Leetcode 3075: Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children/
# Solved on 25th of December, 2025
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        """
        Calculates the maximum happiness sum achievable by selecting k children.

        Args:
            happiness: A list of integers representing the happiness of each child.
            k: An integer representing the number of children to select.
        Returns:
            An integer representing the maximum happiness sum.
        """
        happiness.sort(reverse=True)
        totalHappiness = 0
        for i in range(k):
            val = happiness[i] - i
            if val <= 0:
                break

            totalHappiness += val

        return totalHappiness
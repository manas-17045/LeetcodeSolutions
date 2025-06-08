# Leetcode 1402: Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/
# Solved on 8th of June, 2025

class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        """
        Calculates the maximum total satisfaction that can be obtained by choosing a subset of dishes.

        The satisfaction of a dish is multiplied by its cooking time (which is 1 for the first dish,
        2 for the second, and so on). The total satisfaction is the sum of the satisfaction of all
        chosen dishes.

        Args:
            satisfaction: A list of integers representing the satisfaction value of each dish.
        """
        satisfaction.sort()

        maxCoefficient = 0
        suffixSum = 0

        for i in range(len(satisfaction) -1, -1, -1):
            suffixSum += satisfaction[i]

            if suffixSum <= 0:
                break

            maxCoefficient += suffixSum

        return maxCoefficient
# Leetcode 808: Soup Servings
# https://leetcode.com/problems/soup-servings/
# Resolved on 8th of August, 2025
class Solution:
    def soupServings(self, n: int) -> float:
        """
        Calculates the probability of certain soup serving outcomes.

        Args:
            n (int): The initial amount of soup in milliliters.
        Returns:
            float: The probability of A being empty or A and B being empty simultaneously.
        """
        if n >= 4451:
            return 1.0

        scaledN = (n + 24) // 25
        memo = {}

        def calculateProbability(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            if (a, b) in memo:
                return memo[(a, b)]

            result = 0.25 * (
                    calculateProbability(a - 4, b) +
                    calculateProbability(a - 3, b - 1) +
                    calculateProbability(a - 2, b - 2) +
                    calculateProbability(a - 1, b - 3)
            )

            memo[(a, b)] = result
            return result

        return calculateProbability(scaledN, scaledN)
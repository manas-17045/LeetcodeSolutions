# Leetcode 3693: Climbing Stairs II
# https://leetcode.com/problems/climbing-stairs-ii/
# Solved on 4th of November, 2025
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        """
        Calculates the minimum cost to climb to the top of a staircase with n steps.

        Args:
            n (int): The number of steps in the staircase.
            costs (list[int]): A list where costs[i] is the cost to land on step i+1.

        Returns:
            int: The minimum cost to reach the nth step.
        """
        minCosts = [float('inf')] * (n + 1)
        minCosts[0] = 0

        for currentStep in range(1, n + 1):
            currentCost = costs[currentStep - 1]

            costFromOneBack = minCosts[currentStep - 1] + currentCost + 1
            minCosts[currentStep] = costFromOneBack

            if currentStep - 2 >= 0:
                costFromTwoBack = minCosts[currentStep - 2] + currentCost + 4
                minCosts[currentStep] = min(minCosts[currentStep], costFromTwoBack)

            if currentStep - 3 >= 0:
                costFromThreeBack = minCosts[currentStep - 3] + currentCost + 9
                minCosts[currentStep] = min(minCosts[currentStep], costFromThreeBack)

        return int(minCosts[n])
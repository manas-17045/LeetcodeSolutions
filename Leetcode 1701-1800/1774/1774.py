# Leetcode 1774: Closest Dessert Cost
# https://leetcode.com/problems/closest-dessert-cost/
# Solved on 5th of March, 2026
class Solution:
    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        """
        Finds the closest possible dessert cost to the target using one base and up to two of each topping.

        :param baseCosts: List of costs for each available base.
        :param toppingCosts: List of costs for each available topping.
        :param target: The target cost to approach.
        :return: The cost closest to target. If there is a tie, returns the lower cost.
        """
        bestCost = baseCosts[0]

        def dfs(toppingIndex, currentCost):
            nonlocal bestCost

            if abs(currentCost - target) < abs(bestCost - target):
                bestCost = currentCost
            elif abs(currentCost - target) == abs(bestCost - target) and currentCost < bestCost:
                bestCost = currentCost

            if currentCost >= target or toppingIndex == len(toppingCosts):
                return

            dfs(toppingIndex + 1, currentCost)
            dfs(toppingIndex + 1, currentCost + toppingCosts[toppingIndex])
            dfs(toppingIndex + 1, currentCost + 2 * toppingCosts[toppingIndex])

        for base in baseCosts:
            dfs(0, base)

        return bestCost
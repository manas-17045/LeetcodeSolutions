# Leetcode 3789: Minimum Cost to Acquire Required Items
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
# Solved on 8th of January, 2026
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        """
        Calculates the minimum cost to acquire a certain number of two types of items.

        Args:
            cost1: The cost to acquire one item of type 1.
            cost2: The cost to acquire one item of type 2.
            costBoth: The cost to acquire one item of type 1 and one item of type 2 together.
            need1: The required number of items of type 1.
            need2: The required number of items of type 2.
        Returns:
            The minimum total cost to acquire the required items.
        """
        cost1 = min(cost1, costBoth)
        cost2 = min(cost2, costBoth)

        commonNeed = min(need1, need2)
        totalCost = commonNeed * min(cost1 + cost2, costBoth)

        totalCost += (need1 - commonNeed) * cost1
        totalCost += (need2 - commonNeed) * cost2

        return totalCost
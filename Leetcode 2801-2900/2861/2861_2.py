# Leetcode 2861: Maximum Number of Alloys
# https://leetcode.com/problems/maximum-number-of-alloys/
# Solved on 9th of August, 2025
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: list[list[int]], stock: list[int], cost: list[int]) -> int:
        """
        Calculates the maximum number of alloys that can be produced given a budget and available resources.

        Args:
            n (int): The number of different types of metals.
            k (int): The number of different machines.
            budget (int): The total budget available.
            composition (list[list[int]]): A list of lists where composition[i][j] is the amount of metal j needed by machine i to produce one alloy.
            stock (list[int]): A list where stock[j] is the amount of metal j currently in stock.
            cost (list[int]): A list where cost[j] is the cost of one unit of metal j.

        Returns:
            int: The maximum number of alloys that can be produced.
        """
        # Helper function to check if we can produce x alloys using single machine within budget
        def feasible(x: int) -> bool:
            # Check each machine
            for i in range(k):
                total = 0
                comp_i = composition[i]
                # Accumulate required purchase cost, break early if exceeds budget
                for j in range(n):
                    req = comp_i[j] * x - stock[j]
                    if req > 0:
                        total += req * cost[j]
                        if total > budget:
                            break

                if total <= budget:
                    return True

            return False
        
        # Binary search bounds
        lo, hi = 0, 10**13
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
# Leetcode 3814: Maximum Capacity Within Budget
# https://leetcode.com/problems/maximum-capacity-within-budget/
# Solved on 22nd of January, 2026
import bisect


class Solution:
    def maxCapacity(self, costs: list[int], capacity: list[int], budget: int) -> int:
        """
        Calculates the maximum total capacity achievable by selecting at most two machines
        within the given budget.

        Args:
            costs (list[int]): A list of costs for each machine.
            capacity (list[int]): A list of capacities for each machine.
            budget (int): The maximum total cost allowed.

        Returns:
            int: The maximum total capacity possible.
        """
        n = len(costs)
        machines = sorted(zip(costs, capacity))
        sortedCosts = [m[0] for m in machines]

        prefixMaxCapacity = [0] * n
        currentMax = 0
        for i in range(n):
            currentMax = max(currentMax, machines[i][1])
            prefixMaxCapacity[i] = currentMax

        maxTotalCapacity = 0

        for j in range(n):
            machineCost = machines[j][0]
            machineCap = machines[j][1]

            if machineCost < budget:
                maxTotalCapacity = max(maxTotalCapacity, machineCap)
            else:
                break

            remainingBudget = budget - machineCost
            idx = bisect.bisect_left(sortedCosts, remainingBudget)

            limitIndex = min(j, idx) - 1

            if limitIndex >= 0:
                pairCapacity = machineCap + prefixMaxCapacity[limitIndex]
                maxTotalCapacity = max(maxTotalCapacity, pairCapacity)

        return maxTotalCapacity
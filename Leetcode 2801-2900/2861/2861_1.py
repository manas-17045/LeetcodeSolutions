# Leetcode 2861: Maximum Number of Alloys
# https://leetcode.com/problems/maximum-number-of-alloys/
# Solved on 9th of August, 2025
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: list[list[int]], stock: list[int], cost: list[int]) -> int:
        """
        Calculates the maximum number of alloys that can be created given the available stock, budget,
        and different machine compositions.

        Args:
            n (int): The number of different types of materials.
            k (int): The number of different alloy-making machines.
            budget (int): The total budget available for buying materials.
            composition (list[list[int]]): A list of lists, where composition[j][i] is the amount of material i
                                           needed to create one unit of alloy using machine j.
            stock (list[int]): A list where stock[i] is the current amount of material i available.
            cost (list[int]): A list where cost[i] is the cost of one unit of material i.

        Returns:
            int: The maximum number of alloys that can be created.
        """
        overallMaxAlloys = 0

        maxStock = 0
        if stock:
            maxStock = max(stock)

        for machineComp in composition:
            low = 0
            high = budget + maxStock
            currentMachineMax = 0

            while low <= high:
                numToCreate = low + (high - low) // 2

                if numToCreate == 0:
                    low = numToCreate + 1
                    continue

                requiredCost = 0
                for i in range(n):
                    unitsNeeded = numToCreate * machineComp[i]
                    if unitsNeeded > stock[i]:
                        unitsToBuy = unitsNeeded - stock[i]
                        requiredCost += unitsToBuy * cost[i]

                    if requiredCost > budget:
                        break

                if requiredCost <= budget:
                    currentMachineMax = numToCreate
                    low = numToCreate + 1
                else:
                    high = numToCreate - 1

            overallMaxAlloys = max(overallMaxAlloys, currentMachineMax)

        return overallMaxAlloys
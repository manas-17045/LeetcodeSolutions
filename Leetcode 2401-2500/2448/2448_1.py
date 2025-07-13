# Leetcode 2448: Minimum Cost to Make Array Equal
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/
# Solved on 13th of July, 2025
class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        """
        Calculates the minimum cost to make all elements in `nums` equal.

        Args:
            nums: A list of integers.
            cost: A list of integers representing the cost to change each corresponding number.
        Returns:
            The minimum total cost.
        """
        numAndCost = sorted(zip(nums, cost))

        n = len(nums)
        sortedNums = [item[0] for item in numAndCost]
        sortedCosts = [item[1] for item in numAndCost]

        totalSumOfCosts = sum(sortedCosts)

        weightedSum = 0
        for i in range(n):
            weightedSum += sortedNums[i] * sortedCosts[i]

        currentCost = weightedSum - sortedNums[0] * totalSumOfCosts
        minCost = currentCost

        prefixCostSum = 0
        for i in range(n - 1):
            prefixCostSum += sortedCosts[i]
            gap = sortedNums[i + 1] - sortedNums[i]

            currentCost += gap * (2 * prefixCostSum - totalSumOfCosts)

            minCost = min(minCost, currentCost)

        return minCost
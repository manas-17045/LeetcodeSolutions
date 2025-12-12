# Leetcode 3139: Minimum Cost to Equalize Array
# https://leetcode.com/problems/minimum-cost-to-equalize-array/
# Solved on 12th of December, 2025
class Solution:
    def minCostToEqualizeArray(self, nums: list[int], cost1: int, cost2: int) -> int:
        """
        Calculates the minimum cost to make all elements in the array equal.
        :param nums: A list of integers representing the array.
        :param cost1: The cost to increment a single element by 1.
        :param cost2: The cost to increment two different elements by 1.
        :return: The minimum cost to equalize the array, modulo 10^9 + 7.
        """
        n = len(nums)
        if n == 1:
            return 0

        minVal = min(nums)
        maxVal = max(nums)
        totalSum = sum(nums)
        mod = 10**9 + 7

        if cost1 * 2 <= cost2:
            target = maxVal
            ops = target * n - totalSum
            return (ops * cost1) % mod

        def getCost(target):
            totalOps = target * n - totalSum
            maxDiff = target - minVal

            if maxDiff > totalOps - maxDiff:
                pairedOps = totalOps - maxDiff
                singleOps = maxDiff - pairedOps
                return pairedOps * cost2 + singleOps * cost1
            else:
                pairs = totalOps // 2
                rem = totalOps % 2
                return pairs * cost2 + rem * cost1

        res = float('inf')

        for target in range(maxVal, maxVal + 3):
            res = min(res, getCost(target))

        if n > 2:
            numerator = totalSum - 2 * minVal
            denominator = n - 2
            minTarget = (numerator + denominator - 1) // denominator
            base = max(maxVal, minTarget)

            for target in range(base - 2, base + 3):
                if target >= maxVal:
                    res = min(res, getCost(target))

        return res % mod
# Leetcode 1862: Sum of Floored Pairs
# https://leetcode.com/problems/sum-of-floored-pairs/
# Solved on 18th of August, 2025
class Solution:
    def sumOfFlooredPairs(self, nums: list[int]) -> int:
        """
        Calculates the sum of floored pairs (x // y) for all pairs (x, y) from the input list `nums`.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The sum of floored pairs modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7

        if not nums:
            return 0

        maxVal = max(nums)

        counts = [0] * (maxVal + 1)
        for num in nums:
            counts[num] += 1

        prefixCounts = [0] * (maxVal + 1)
        for i in range(1, maxVal + 1):
            prefixCounts[i] = prefixCounts[i - 1] + counts[i]

        totalSum = 0
        for y in range(1, maxVal + 1):
            if counts[y] == 0:
                continue

            sumForY = 0
            for m in range(y, maxVal + 1, y):
                k = m // y

                lowerBound = m
                upperBound = min(m + y - 1, maxVal)

                countInRange = prefixCounts[upperBound] - prefixCounts[lowerBound - 1]

                sumForY = (sumForY + k * countInRange) % mod

            totalSum = (totalSum + sumForY * counts[y]) % mod

        return totalSum
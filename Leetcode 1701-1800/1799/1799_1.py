# Leetcode 1799: Maximize Score After N Operations
# https://leetcode.com/problems/maximize-score-after-n-operations/
# Solved on 11th of June, 2025
import math


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        """
        Calculates the maximum score achievable after performing n operations.

        In each operation, we select two elements from the array, calculate their
        greatest common divisor (GCD), multiply it by the operation number (starting
        from 1), and add it to the score. The selected elements are then removed.

        Args:
            nums: A list of integers.

        Returns:
            The maximum possible score.
        """
        numLen = len(nums)
        dp = [0] * (1 << numLen)

        for mask in range(1, 1 << numLen):
            bitsSet = bin(mask).count('1')
            if bitsSet % 2 != 0:
                continue

            operationNum = bitsSet // 2

            for i in range(numLen):
                if (mask >> i) & 1:
                    for j in range(i + 1, numLen):
                        if (mask >> j) & 1:
                            prevMask = mask ^ (1 << i) ^ (1 << j)
                            currentGcd = math.gcd(nums[i], nums[j])
                            score = dp[prevMask] + operationNum * currentGcd
                            dp[mask] = max(dp[mask], score)

        return dp[(1 << numLen) - 1]
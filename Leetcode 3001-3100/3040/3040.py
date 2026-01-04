# Leetcode 3040: Maximum Number of Operations With the Same Score II
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/
# Solved on 4th of January, 2026
import sys
from functools import lru_cache
sys.setrecursionlimit(5000)


class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        """
        Calculates the maximum number of operations that can be performed on the array `nums`.
        An operation consists of removing two elements whose sum equals a predefined target.
        The target sum is determined by the first operation.

        Args:
            nums: A list of integers.
        Returns:
            The maximum number of operations.
        """
        n = len(nums)

        @lru_cache(None)
        def solve(i, j, target):
            if i >= j:
                return 0

            res = 0
            if nums[i] + nums[i + 1] == target:
                res = max(res, 1 + solve(i + 2, j, target))
            if nums[j] + nums[j - 1] == target:
                res = max(res, 1 + solve(i, j - 2, target))
            if nums[i] + nums[j] == target:
                res = max(res, 1 + solve(i + 1, j - 1, target))

            return res

        result = 0

        term1 = nums[0] + nums[1]
        result = max(result, 1 + solve(2, n - 1, term1))

        term2 = nums[n - 1] + nums[n - 2]
        result = max(result, 1 + solve(0, n - 3, term2))

        term3 = nums[0] + nums[n - 1]
        result = max(result, 1 + solve(1, n - 2, term3))

        return result

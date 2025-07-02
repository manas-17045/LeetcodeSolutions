# Leetcode 1770: Maximum Score from Performing Multiplication Operations
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
# Solved on 2nd of July, 2025
from functools import lru_cache


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        """
        Calculates the maximum score achievable by performing a series of operations.

        In each operation, you choose either the leftmost or the rightmost element
        from the `nums` array and multiply it by the current multiplier from the
        `multipliers` array. The chosen element is then removed from `nums`.
        This process continues for `m` operations, where `m` is the length of
        `multipliers`.

        Args:
            nums: A list of integers representing the initial array.
            multipliers: A list of integers representing the multipliers for each operation.
        Returns:
            The maximum possible score.
        """
        n, m = len(nums), len(multipliers)
        # Use recursion with memoization: state (i, left_picks)
        @lru_cache(None)
        def dp(i: int, left: int) -> int:
            # i operations performed, left elements taken from the start
            if i == m:
                return 0

            # Current multiplier
            mult = multipliers[i]
            # Choose left element at index left
            left_score = nums[left] * mult + dp((i + 1), (left + 1))
            # Choose right element at index right
            right_index = n - 1 - (i - left)
            right_score = nums[right_index] * mult + dp((i + 1), left)
            return max(left_score, right_score)

        return dp(0, 0)
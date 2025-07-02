# Leetcode 1770: Maximum Score from Performing Multiplication Operations
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
# Solved on 2nd of July, 2025
class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        """
        Calculates the maximum score obtainable from performing multiplication operations.

        Args:
            nums: A list of integers representing the numbers.
            multipliers: A list of integers representing the multipliers.

        Returns:
            The maximum score.
        """
        n = len(nums)
        m = len(multipliers)
        memo = {}

        def solve(i, left):
            if i == m:
                return 0

            state = (i, left)
            if state in memo:
                return memo[state]

            right = n - 1 - (i - left)

            pickLeft = multipliers[i] * nums[left] + solve((i + 1), (left + 1))
            pickRight = multipliers[i] * nums[right] + solve((i + 1), left)

            memo[state] = max(pickLeft, pickRight)
            return memo[state]

        return solve(0, 0)
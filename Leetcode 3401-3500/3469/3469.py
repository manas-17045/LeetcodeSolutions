# Leetcode 3469: Find Minimum Cost to Remove Array Elements
# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/
# Solved on 1st of December, 2025
class Solution:
    def minCost(self, nums: list[int]) -> int:
        """
        Calculates the minimum cost to remove all elements from the array.

        Args:
            nums: A list of integers representing the array.
        Returns:
            The minimum cost to remove all elements.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo = [[-1] * n for _ in range(n + 1)]

        def solve(index, prevIndex):
            if index >= n:
                return nums[prevIndex]
            if index == n - 1:
                return max(nums[prevIndex], nums[index])

            if memo[index][prevIndex] != -1:
                return memo[index][prevIndex]

            costOne = max(nums[prevIndex], nums[index]) + solve(index + 2, index + 1)
            costTwo = max(nums[prevIndex], nums[index + 1]) + solve(index + 2, index)
            costThree = max(nums[index], nums[index + 1]) + solve(index + 2, prevIndex)

            result = min(costOne, costTwo, costThree)
            memo[index][prevIndex] = result
            return result

        return solve(1, 0)
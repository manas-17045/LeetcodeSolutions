# Leetcode 3840: House Robber V
# https://leetcode.com/problems/house-robber-v/
# Solved on 16th of February, 2026
class Solution:
    def rob(self, nums: list[int], colors: list[int]) -> int:
        """
        Calculates the maximum loot possible by robbing houses of different colors.
        Houses of the same color are treated as a standard House Robber subproblem.

        :param nums: List of integers representing the amount of money in each house.
        :param colors: List of integers representing the color of each house.
        :return: The maximum total loot possible.
        """
        totalLoot = 0
        prevMax = 0
        currMax = 0
        n = len(nums)

        for i in range(n):
            temp = currMax
            if prevMax + nums[i] > currMax:
                currMax = prevMax + nums[i]

            prevMax = temp

            if i == n - 1 or colors[i] != colors[i + 1]:
                totalLoot += currMax
                prevMax = 0
                currMax = 0

        return totalLoot
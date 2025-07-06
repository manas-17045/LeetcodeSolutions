# Leetcode 3194: Minimum Average of Smallest and Largest Elements
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
# Solved on 6th of July, 2025
class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        """
        Calculates the minimum average obtained by repeatedly removing the smallest
        and largest elements from the array and computing their average.

        Args:
            nums: A list of integers.

        Returns:
            The minimum average found.
        """
        nums.sort()

        minAverage = float('inf')

        left = 0
        right = len(nums) - 1

        while left < right:
            currentAverage = (nums[left] + nums[right]) / 2
            minAverage = min(minAverage, currentAverage)
            left += 1
            right -= 1

        return minAverage
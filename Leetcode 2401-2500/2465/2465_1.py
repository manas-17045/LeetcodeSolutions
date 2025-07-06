# Leetcode 2465: Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/
# Solved on 6th of July, 2025
class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        """
        Calculates the number of distinct averages formed by repeatedly removing
        the smallest and largest elements from the array and calculating their average.

        Args:
            nums: A list of integers.

        Returns:
            The number of distinct averages.
        """
        nums.sort()

        distinctAverages = set()
        leftIndex = 0
        rightIndex = len(nums) - 1

        while leftIndex < rightIndex:
            currentAverage = (nums[leftIndex] + nums[rightIndex]) / 2
            distinctAverages.add(currentAverage)
            leftIndex += 1
            rightIndex -= 1

        return len(distinctAverages)
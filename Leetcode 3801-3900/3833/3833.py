# Leetcode 3833: Count Dominant Indices
# https://leetcode.com/problems/count-dominant-indices/
# Solved on 9th of February, 2026
class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        """
        Counts the number of indices i such that nums[i] is greater than the average
        of all elements to its right.

        :param nums: A list of integers to evaluate.
        :return: The total count of dominant indices.
        """
        n = len(nums)
        dominantCount = 0
        runningSum = 0
        elementsToRight = 0

        for i in range(n - 1, -1, -1):
            if elementsToRight > 0:
                if nums[i] * elementsToRight > runningSum:
                    dominantCount += 1

            runningSum += nums[i]
            elementsToRight += 1

        return dominantCount
# Leetcode 3678: Smallest Absent Positive Greater Than Average
# https://leetcode.com/problems/smallest-absent-positive-greate-than-average/
# Solved on 1st of April, 2026
class Solution:
    def smallestNumber(self, nums: list[int]) -> int:
        """
        Finds the smallest positive integer greater than the average of the list that is not present in the list.

        :param nums: A list of integers.
        :return: The smallest absent positive integer greater than the average.
        """
        numSet = set(nums)
        currentVal = max(1, sum(nums) // len(nums) + 1)

        while currentVal in numSet:
            currentVal += 1

        return currentVal
# Leetcode 2592: Maximize Greatness of an Array
# https://leetcode.com/problems/maximize-greatness-of-an-array/
# Solved on 16th of November, 2025
class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        """
        Maximizes the greatness of an array.

        Args:
            nums: A list of integers.

        Returns:
            The maximum possible greatness count.
        """
        nums.sort()
        n = len(nums)
        greatnessCount = 0
        i = 0
        j = 0

        while i < n and j < n:
            if nums[j] > nums[i]:
                greatnessCount += 1
                i += 1
                j += 1
            else:
                j += 1

        return greatnessCount
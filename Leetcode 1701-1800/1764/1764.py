# Leetcode 1764: Form Array by Concatenating Subarrays of Another Array
# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
# Solved on 10th of November, 2025
class Solution:
    def canChoose(self, groups: list[list[int]], nums: list[int]) -> bool:
        """
        Determines if all groups can be formed by concatenating non-overlapping subarrays of nums.

        Args:
            groups (list[list[int]]): A list of integer arrays representing the groups to be found.
            nums (list[int]): An integer array from which to form the groups.

        Returns:
            bool: True if all groups can be formed, False otherwise.
        """
        numsIndex = 0
        groupIndex = 0

        lenNums = len(nums)
        lenGroups = len(groups)

        while numsIndex < lenNums and groupIndex < lenGroups:
            currentGroup = groups[groupIndex]
            lenCurrentGroup = len(currentGroup)

            if numsIndex + lenCurrentGroup <= lenNums and nums[numsIndex: numsIndex + lenCurrentGroup] == currentGroup:
                numsIndex += lenCurrentGroup
                groupIndex += 1
            else:
                numsIndex += 1

        return groupIndex == lenGroups
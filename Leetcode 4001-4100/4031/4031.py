# Leetcode 4031: Find All Numbers Disappeared in an Array II
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/
# Solved on 23rd of September, 2026
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        """
        Find contiguous ranges of missing integers within the inclusive range [lower, upper].

        Parameters:
            nums (list[int]): The input array of integers.
            lower (int): The lower boundary of the target range.
            upper (int): The upper boundary of the target range.

        Returns:
            list[list[int]]: A list of ranges [start, end] denoting missing numbers.
        """
        nums.sort()
        missingRanges = []
        expectedNum = lower

        for currentNum in nums:
            if currentNum < expectedNum:
                continue

            if currentNum > upper:
                break

            if currentNum > expectedNum:
                missingRanges.append([expectedNum, currentNum - 1])

            expectedNum = currentNum + 1

        if expectedNum <= upper:
            missingRanges.append([expectedNum, upper])

        return missingRanges
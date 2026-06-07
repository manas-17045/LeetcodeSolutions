# Leetcode 3940: Limit Occurrences in Sorted Array
# https://leetcode.com/problems/limit-occurrences-in-sorted-array/
# Solved on 7th of June, 2026
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        """
        Modifies a sorted array in-place to ensure each element appears at most k times.

        :param nums: A list of integers sorted in non-decreasing order.
        :param k: The maximum number of allowed occurrences for any single integer.
        :return: The modified list containing elements with limited occurrences.
        """
        if len(nums) <= k:
            return nums

        writeIdx = k
        for readIdx in range(k, len(nums)):
            if nums[readIdx] != nums[writeIdx - k]:
                nums[writeIdx] = nums[readIdx]
                writeIdx += 1

        return nums[:writeIdx]
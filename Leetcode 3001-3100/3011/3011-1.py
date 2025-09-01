# Leetcode 3011: Find if Array can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/
# Solved on 1st of September, 2025
class Solution:
    def canBeSorted(self, nums: list[int]) -> bool:
        """
        Checks if the given array `nums` can be sorted by swapping adjacent elements
        within chunks where all elements in a chunk have the same number of set bits.
        :param nums: A list of integers.
        :return: True if the array can be sorted, False otherwise.
        """
        listLength = len(nums)
        chunkStart = 0
        maxOfPreviousChunk = 0

        while chunkStart < listLength:
            currentSetBits = nums[chunkStart].bit_count()
            minOfCurrentChunk = nums[chunkStart]
            maxOfCurrentChunk = nums[chunkStart]

            chunkEnd = chunkStart + 1
            while chunkEnd < listLength and nums[chunkEnd].bit_count() == currentSetBits:
                minOfCurrentChunk = min(minOfCurrentChunk, nums[chunkEnd])
                maxOfCurrentChunk = max(maxOfCurrentChunk, nums[chunkEnd])
                chunkEnd += 1

            if minOfCurrentChunk < maxOfPreviousChunk:
                return False

            maxOfPreviousChunk = maxOfCurrentChunk
            chunkStart = chunkEnd

        return True
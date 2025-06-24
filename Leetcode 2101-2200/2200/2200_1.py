# Leetcode 2200: Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# Solved on 24th of June, 2025
class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        Finds all indices i such that there exists at least one index j where nums[j] == key
        and |i - j| <= k.

        Args:
            nums: A list of integers.
            key: The integer value to search for in `nums`.
            k: The maximum allowed distance from an index `j` (where `nums[j] == key`).

        Returns:
            A sorted list of all k-distant indices.
        """
        numLength = len(nums)
        keyIndices = []

        for i in range(numLength):
            if nums[i] == key:
                keyIndices.append(i)

        rawIntervals = []
        for keyIdx in keyIndices:
            intervalStart = max(0, (keyIdx - k))
            intervalEnd = min((numLength - 1), (keyIdx + k))
            rawIntervals.append([intervalStart, intervalEnd])

        mergedIntervals = []

        # Constraints guarantee keyIndices is not empty, so rawIntervals is not empty.
        mergedIntervals.append(rawIntervals[0])

        for i in range(1, len(rawIntervals)):
            currentIntervalStart, currentIntervalEnd = rawIntervals[0]

            lastMergedIntervalEnd = mergedIntervals[-1][1]

            if currentIntervalStart <= lastMergedIntervalEnd + 1:
                mergedIntervals[-1][1] = max(lastMergedIntervalEnd, currentIntervalEnd)
            else:
                mergedIntervals.append(rawIntervals[i])

        resultIndices = []
        for intervalStart, intervalEnd in mergedIntervals:
            for idxToAdd in range(intervalStart, (intervalEnd + 1)):
                resultIndices.append(idxToAdd)

        return resultIndices
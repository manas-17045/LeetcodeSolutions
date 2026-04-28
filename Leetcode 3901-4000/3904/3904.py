# Leetcode 3904: Smallest Stable Index II
# https://leetcode.com/problems/smallest-stable-index-ii/
# Solved on 28th of April, 2026
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        """
        Finds the smallest index i such that the difference between the maximum element
        in the prefix nums[0...i] and the minimum element in the suffix nums[i...n-1] is at most k.

        :param nums: A list of integers.
        :param k: The maximum allowed difference (stability threshold).
        :return: The smallest stable index i, or -1 if no such index exists.
        """
        listLength = len(nums)
        suffMin = [0] * listLength
        currentMin = nums[listLength - 1]

        for i in range(listLength - 1, -1, -1):
            if nums[i] < currentMin:
                currentMin = nums[i]
            suffMin[i] = currentMin

        currentMax = nums[0]

        for i in range(listLength):
            if nums[i] > currentMax:
                currentMax = nums[i]
            if currentMax - suffMin[i] <= k:
                return i

        return -1
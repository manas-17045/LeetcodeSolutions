# Leetcode 3903: Smallest Stable Index I
# https://leetcode.com/problems/smallest-stable-index/
# Solved on 28th of April, 2026
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        """
        Finds the smallest index i such that the difference between the maximum element
        in the prefix nums[0...i] and the minimum element in the suffix nums[i...n-1]
        is at most k.

        :param nums: A list of integers.
        :param k: The maximum allowed instability score.
        :return: The smallest stable index i, or -1 if no such index exists.
        """
        listLen = len(nums)
        suffixMin = [0] * listLen
        suffixMin[-1] = nums[-1]

        for i in range(listLen - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        currentMax = nums[0]

        for i in range(listLen):
            currentMax = max(currentMax, nums[i])
            instabilityScore = currentMax - suffixMin[i]

            if instabilityScore <= k:
                return i

        return -1
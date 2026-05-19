# Leetcode 3920: Maximize Fixed Points After Deletions
# https://leetcode.com/problems/maximize-fixed-points-after-deletions/
# Solved on 19th of May, 2026
class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        """
        Calculates the maximum number of fixed points (nums[i] == i) that can be achieved
        after deleting any number of elements from the array.

        :param nums: A list of integers.
        :return: The maximum number of fixed points possible.
        """
        validPairs = []
        for index, val in enumerate(nums):
            if index >= val:
                validPairs.append((val, index - val))

        validPairs.sort(key=lambda item: (item[0], -item[1]))

        optimalDiffs = []
        for _, diff in validPairs:
            leftIndex = 0
            rightIndex = len(optimalDiffs)
            while leftIndex < rightIndex:
                midIndex = (leftIndex + rightIndex) // 2
                if optimalDiffs[midIndex] <= diff:
                    leftIndex = midIndex + 1
                else:
                    rightIndex = midIndex

            if leftIndex == len(optimalDiffs):
                optimalDiffs.append(diff)
            else:
                optimalDiffs[leftIndex] = diff

        return len(optimalDiffs)
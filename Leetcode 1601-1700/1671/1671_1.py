# Leetcode 1671: Minimum Number of Removals to Make Mountain Array
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
# Solved on 25th of July, 2025
import bisect


class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of removals to make a mountain array.

        Args:
            nums (list[int]): The input array of integers.
        Returns:
            int: The minimum number of elements to remove to form a mountain array.
        """

        numCount = len(nums)

        leftPart = [0] * numCount
        sub = []
        for i in range(numCount):
            currentNum = nums[i]
            index = bisect.bisect_left(sub, currentNum)
            if index == len(sub):
                sub.append(currentNum)
            else:
                sub[index] = currentNum

            leftPart[i] = index + 1

        rightPart = [0] * numCount
        sub = []
        for i in range(numCount - 1, -1, -1):
            currentNum = nums[i]
            index = bisect.bisect_left(sub, currentNum)
            if index == len(sub):
                sub.append(currentNum)
            else:
                sub[index] = currentNum

            rightPart[i] = index + 1

        maxLen = 0
        for i in range(numCount):
            if leftPart[i] > 1 and rightPart[i] > 1:
                currentLen = leftPart[i] + rightPart[i] - 1
                maxLen = max(maxLen, currentLen)

        return numCount - maxLen
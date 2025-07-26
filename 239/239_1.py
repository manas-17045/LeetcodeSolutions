# Leetcode 239: Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
# Solved on 26th of July, 2025
import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the maximum value in each sliding window of size k.

        :param nums: The input list of integers.
        :param k: The size of the sliding window.
        :return: A list containing the maximum value for each sliding window.
        """

        outputList = []
        indexQueue = collections.deque()

        for rightPointer in range(len(nums)):
            if indexQueue and indexQueue[0] == rightPointer - k:
                indexQueue.popleft()

            while indexQueue and nums[indexQueue[-1]] < nums[rightPointer]:
                indexQueue.pop()

            indexQueue.append(rightPointer)

            if rightPointer >= k - 1:
                outputList.append(nums[indexQueue[0]])

        return outputList
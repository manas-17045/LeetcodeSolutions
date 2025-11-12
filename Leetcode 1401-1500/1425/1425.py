# Leetcode 1425: Constrained Subsequence Sum
# https://leetcode.com/problems/constrained-subsequence-sum/
# Solved on 12th of November, 2025
import collections


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum sum of a non-empty subsequence such that for any two consecutive
        integers nums[i] and nums[j] in the subsequence with i < j, the condition j - i <= k is satisfied.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum allowed difference between indices of consecutive elements.
        Returns:
            The maximum sum of a constrained subsequence.
        """
        indexQueue = collections.deque()
        maxOverallSum = float('-inf')

        for i in range(len(nums)):
            if indexQueue and indexQueue[0] < (i - k):
                indexQueue.popleft()

            maxPreviousSum = nums[indexQueue[0]] if indexQueue else 0

            currentSum = nums[i] + max(0, maxPreviousSum)
            nums[i] = currentSum

            while indexQueue and nums[indexQueue[-1]] < nums[i]:
                indexQueue.pop()

            indexQueue.append(i)

            maxOverallSum = max(maxOverallSum, nums[i])

        return maxOverallSum
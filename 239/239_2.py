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
        :return: A list of maximum values for each window.
        """

        if not nums or k == 0:
            return []

        n = len(nums)
        # Will store the indices of elements, in decreasing order of their values
        dq = collections.deque()
        result = []

        for i in range(n):
            # Remove indices that are out of the current window [i-k+1, i]
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order in dq
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Starting at i = k - 1, the front of the deque is the max for the window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
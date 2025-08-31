# Leetcode 1696: Jump Game VI
# https://leetcode.com/problems/jump-game-vi/
# Solved on 31st of August, 2025
from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum score reachable from the first index to the last index.

        Args:
            nums (list[int]): A list of integers representing the scores at each position.
            k (int): The maximum number of steps you can jump forward.
        Returns:
            int: The maximum score reachable.
        """

        numsLength = len(nums)
        scoreDeque = deque([0])

        for i in range(1, numsLength):
            if scoreDeque[0] < i - k:
                scoreDeque.popleft()

            nums[i] += nums[scoreDeque[0]]

            while scoreDeque and nums[scoreDeque[-1]] <= nums[i]:
                scoreDeque.pop()

            scoreDeque.append(i)

        return nums[numsLength - 1]
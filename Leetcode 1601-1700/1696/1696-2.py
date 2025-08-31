# Leetcode 1696: Jump Game VI
# https://leetcode.com/problems/jump-game-vi/
# Solved on 31st of August, 2025
from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum score reachable at the last index of the array.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The maximum jump distance.
        Returns:
            int: The maximum score reachable at the last index.
        """

        n = len(nums)
        # deque will store indices, with nums[idx] being non-increasing
        dq = deque([0])
        # nums[0] is already the score to reach index 0
        for i in range(1, n):
            # Pop indices out of window (older than (i - k))
            while dq and dq[0] < i - k:
                dq.popleft()

            # Best previous dp is at dp[0]
            nums[i] = nums[i] + nums[dq[0]]
            # Maintain deque monotonic decreasing by dp value (nms[...])
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

        return nums[-1]
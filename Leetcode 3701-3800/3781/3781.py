# Leetcode 3781: Maximum Score After Binary Swaps
# https://leetcode.com/problems/maximum-score-after-binary-swaps/
# Solved on 25th of December, 2025
import heapq


class Solution:
    def maximumScore(self, nums: list[int], s: str) -> int:
        """
        Calculates the maximum score after binary swaps.

        Args:
            nums: A list of integers.
            s: A binary string of the same length as nums.

        Returns:
            The maximum score achievable.
        """
        n = len(nums)
        minHeap = []
        onesCount = 0

        for i in range(n - 1, -1, -1):
            heapq.heappush(minHeap, nums[i])

            if s[i] == '1':
                onesCount += 1

            if len(minHeap) > onesCount:
                heapq.heappop(minHeap)

        return sum(minHeap)
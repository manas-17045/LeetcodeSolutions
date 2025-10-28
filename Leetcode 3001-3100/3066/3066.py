# Leetcode 3066: Minimum Operations to Exceed Threshold Value II
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
# Solved on 28th of October, 2025
import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to make all elements in `nums`
        greater than or equal to `k`.

        :param nums: A list of integers.
        :param k: The threshold value.
        :return: The minimum number of operations.
        """
        heapq.heapify(nums)
        operationCount = 0

        while nums[0] < k:
            firstSmallest = heapq.heappop(nums)
            secondSmallest = heapq.heappop(nums)

            newValue = (firstSmallest * 2) + secondSmallest

            heapq.heappush(nums, newValue)
            operationCount += 1

        return operationCount
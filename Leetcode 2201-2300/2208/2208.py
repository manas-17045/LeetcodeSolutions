# Leetcode 2208: Minimum Operations to Halve Array Sum
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
# Solved on 30th of November, 2025
import heapq


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to reduce the total sum of an array by at least half.
        In each operation, you can choose any number in the array and reduce it by half.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations required.
        """
        totalSum = sum(nums)
        targetReduction = totalSum / 2
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        accumulatedReduction = 0
        operationCount = 0

        while accumulatedReduction < targetReduction:
            maxValue = -heapq.heappop(maxHeap)
            reductionAmount = maxValue / 2
            accumulatedReduction += reductionAmount
            heapq.heappush(maxHeap, -reductionAmount)
            operationCount += 1

        return operationCount
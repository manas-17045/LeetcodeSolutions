# Leetcode 1354: Construct Target Array With Multiple Sums
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/
# Solved on 28th of September, 2025
import heapq


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        """
        Determines if a given target array can be constructed starting from an array of ones.
        The construction rule is: in each step, replace the largest element with the sum of the remaining elements.

        Args:
            target (list[int]): The target array of integers.
        Returns:
            bool: True if the target array can be constructed, False otherwise.
        """
        numElements = len(target)

        if numElements == 1:
            return target[0] == 1

        totalSum = sum(target)
        maxHeap = [-value for value in target]
        heapq.heapify(maxHeap)

        while -maxHeap[0] > 1:
            maxValue = -heapq.heappop(maxHeap)
            restSum = totalSum - maxValue

            if restSum == 1:
                return True

            if maxValue <= restSum or restSum == 0:
                return False

            previousValue = maxValue % restSum

            if previousValue == 0:
                return False

            totalSum = restSum + previousValue
            heapq.heappush(maxHeap, -previousValue)

        return True
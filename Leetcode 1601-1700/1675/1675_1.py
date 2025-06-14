# Leetcode 1675: Minimize Deviation in Array
# https://leetcode.com/problems/minimize-deviation-in-array/
# Solved on 14th of June, 2025
import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        """
        Calculates the minimum deviation of an array.

        The deviation of an array is the maximum difference between any two
        elements in the array. You can perform two operations on the array:
        1. If an element is odd, you can multiply it by 2.
        2. If an element is even, you can divide it by 2.

        The goal is to minimize the deviation by applying these operations any
        number of times.

        The strategy is to first transform all odd numbers to their doubled
        value (making them even), as this is the only operation allowed on odd
        numbers to potentially increase their value. Then, we maintain a max-heap
        of the current numbers and the minimum value encountered so far. We
        repeatedly reduce the maximum element (if it's even) by dividing it by 2,
        updating the minimum value and the minimum deviation as we go. This process
        continues until the maximum element is odd, at which point we can no longer
        reduce it.
        """
        maxHeap = []
        minVal = float('inf')

        for num in nums:
            if num % 2 == 1:
                transformedNum = num * 2
            else:
                transformedNum = num

            heapq.heappush(maxHeap, -transformedNum)
            minVal = min(minVal, transformedNum)

        minDeviation = -maxHeap[0] - minVal

        while -maxHeap[0] % 2 == 0:
            currentMax = -heapq.heappop(maxHeap)

            reducedMax = currentMax // 2
            heapq.heappush(maxHeap, -reducedMax)
            minVal = min(minVal, reducedMax)

            newMax = -maxHeap[0]
            minDeviation = min(minDeviation, (newMax - minVal))

        return minDeviation
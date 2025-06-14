# Leetcode 1675: Minimize Deviation in Array
# https://leetcode.com/problems/minimize-deviation-in-array/
# Solved on 14th of June, 2025
import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        """
        Calculates the minimum deviation of an array of numbers.

        The deviation of an array is the maximum difference between any two elements.
        You can perform two operations on the array:
        1. If an element is even, you can divide it by 2.
        2. If an element is odd, you can multiply it by 2.

        Args:
            nums: A list of integers.
        """
        # Make every number even by doubling odds.
        # This gives us an initial upper bound on each element.
        heap = []
        current_min = float('inf')
        for x in nums:
            if x & 1:   # If odd
                x <<= 1 # Make even
            current_min = min(current_min, x)
            heap.append(-x) # We use a max-heap via negatives

        heapq.heapify(heap)
        ans = float('inf')

        # While the current maximum is even, we can halve it to try to reduce deviation
        while True:
            current_max = -heap[0]
            ans = min(ans, (current_max - current_min))

            # If the max is odd, we can't reduce it further; we're done.
            if current_max & 1:
                break

            # Otherwise, halve it and restart.
            heapq.heappop(heap)
            new_val = current_max >> 1
            current_min = min(current_min, new_val)
            heapq.heappush(heap, -new_val)

        return ans
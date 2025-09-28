# Leetcode 1354: Construct Target Array With Multiple Sums
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/
# Solved on 28th of September, 2025
import heapq


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        """
        Determines if a given target array can be formed by starting with an array of ones
        and repeatedly applying a specific operation.

        Args:
            target: A list of integers representing the target array.
        Returns:
            True if the target array is possible, False otherwise.
        """
        if not target:
            return False
        n = len(target)
        if n == 1:
            return target[0] == 1

        # Use a max-heap (store negatives)
        heap = [-x for x in target]
        heapq.heapify(heap)
        total = sum(target)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            # If the largest is 1, all are 1
            if largest == 1 or rest == 1:
                return True

            # Invalid cases
            if rest == 0 or largest < rest:
                return False

            # Find the previous value of 'largest' before the last operation
            prev = largest % rest

            if prev == 0:
                return False

            # Update total and push previous value back into heap
            total = rest + prev
            heapq.heappush(heap, -prev)
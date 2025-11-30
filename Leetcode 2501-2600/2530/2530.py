# Leetcode 2530: Maximal Score After Applying K Operations
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/
# Solved on 30th of November, 2025
import heapq


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximal score after applying k operations.

        Args:
            nums: A list of integers representing the initial numbers.
            k: An integer representing the number of operations to apply.
        Returns:
            An integer representing the maximal score.
        """
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        totalScore = 0

        for _ in range(k):
            currentVal = -heapq.heappop(maxHeap)
            totalScore += currentVal
            nextVal = (currentVal + 2) // 3
            heapq.heappush(maxHeap, -nextVal)

        return totalScore
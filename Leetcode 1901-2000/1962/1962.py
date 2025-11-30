# Leetcode 1962: Remove Stones to Minimize the Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
# Solved on 30th of November, 2025
import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        """
        Removes stones from piles to minimize the total sum.

        Args:
            piles: A list of integers representing the number of stones in each pile.
            k: An integer representing the number of operations to perform.
        Returns:
            The minimum possible total sum of stones after k operations.
        """
        maxHeap = [-pile for pile in piles]
        heapq.heapify(maxHeap)

        for _ in range(k):
            currentPile = -heapq.heappop(maxHeap)
            removeVal = currentPile // 2
            currentPile -= removeVal
            heapq.heappush(maxHeap, -currentPile)

        return -sum(maxHeap)
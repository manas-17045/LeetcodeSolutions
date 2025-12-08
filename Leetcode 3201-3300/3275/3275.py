# Leetcode 3275: K-th Nearest Obstacle Queries
# https://leetcode.com/problems/k-th-nearest-obstacle-queries/
# Solved on 8th of December, 2025
import heapq


class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        """
        Calculates the k-th nearest obstacle distance for a series of queries.

        Args:
            queries: A list of [x, y] coordinates representing obstacle queries.
            k: The k-th nearest obstacle to find.

        Returns:
            A list of integers, where each element is the k-th nearest obstacle distance for the corresponding query.
        """

        maxHeap = []
        results = []

        for x, y in queries:
            distance = abs(x) + abs(y)
            heapq.heappush(maxHeap, -distance)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

            if len(maxHeap) < k:
                results.append(-1)
            else:
                results.append(-maxHeap[0])

        return results
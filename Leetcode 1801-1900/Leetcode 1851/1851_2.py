# Leetcode 1851: Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Solved on 15th of May, 2025
import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """
        Finds the smallest interval that includes each query.

        Args:
            intervals: A list of intervals, where each interval is a list [start, end].
            queries: A list of query integers.

        Returns:
            A list of integers, where each integer is the length of the smallest interval
            that includes the corresponding query.  Returns -1 if no interval includes
            the query.

        """

        # Sort intervals by start ascending
        intervals.sort(key=lambda x: x[0])

        # Pair each query with its original index, and sort by query value
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        ans = [-1] * len(queries)
        min_heap = []   # will store (length, end) for intervals whose start <= current query
        i = 0
        n = len(intervals)

        for qval, qidx in sorted_queries:
            # Add all intervals that begin on or before qval
            while i < n and intervals[i][0] <= qval:
                l, r = intervals[i]
                length = r - l + 1
                heapq.heappush(min_heap, (length, r))
                i += 1

            # Remove any intervals that end before qval (they don't cover qval)
            while min_heap and min_heap[0][1] < qval:
                heapq.heappop(min_heap)

            # Top of heap is now the smallest-length interval covering qval (if any)
            if min_heap:
                ans[qidx] = min_heap[0][0]

        return ans
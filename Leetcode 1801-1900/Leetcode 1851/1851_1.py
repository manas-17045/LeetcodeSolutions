# Leetcode 1851: Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Solved on 15th of May, 2025
import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """
        Finds the minimum size interval that includes each query.

        Given a list of intervals and a list of queries, this function determines, for each query,
        the smallest interval that contains it.  If no interval contains a query, the result is -1.

        Args:
            intervals: A list of intervals, where each interval is represented as a list [start, end].
            queries: A list of integers representing the queries.

        Returns:
            A list of integers, where each integer is the size of the smallest interval containing the
            corresponding query, or -1 if no interval contains the query.
        """

        # Sort intervals by their start points.
        # This allows us to efficiently add intervals that could cover upcoming queries
        # as we process queries in increasing order of their values
        intervals.sort(key=lambda x: x[0])

        num_queries = len(queries)
        # Initialize the answer array with -1 (default for no covering interval).
        ans = [-1] * num_queries

        # To process queries in increasing order of their values while preserving original indices:
        # Create a list of tuples: (query_value, original_index).
        # This allows us to sort queries by value but still populate the 'ans' array
        # in the correct order corresponding to the original 'queries' input.
        sorted_queries_with_indices = []
        for i in range(num_queries):
            sorted_queries_with_indices.append((queries[i], i))

        # Sort by query_value
        sorted_queries_with_indices.sort(key=lambda x: x[0])

        # Min-heap to store active intervals.
        # An interval is "active" for a query q_val if its left endpoint <= q_val.
        # The heap stores tuples of (interval_size, right_endpoint).
        # It's ordered by interval_size, so we can quickly get the smallest site.
        active_intervals_heap = []

        # Pointer for iterating through the sorted 'intervals' array.
        interval_ptr = 0
        num_intervals = len(intervals)

        # Iterate through the queries, sorted by their values:
        for q_val, original_idx in sorted_queries_with_indices:
            # Add all intervals whose start point is less than or equal to the current query value.
            # These intervals become candidates to cover the current query q_val.
            # They are added to the min-heap.
            while interval_ptr < num_intervals and intervals[interval_ptr][0] <= q_val:
                left, right = intervals[interval_ptr]
                size = right - left + 1
                # Push (size, right_endpoint) onto the heap.
                heapq.heappush(active_intervals_heap, (size, right))
                interval_ptr += 1

            # Remove intervals from the heap that no longer cover the current query q_val.
            # An interval [L, R] does not cover q_val if its right_endpoint R < q_val.
            while active_intervals_heap and active_intervals_heap[0][1] < q_val:
                heapq.heappop(active_intervals_heap)

            # If the heap is not empty after additions and removals,
            # the top element's size is the minimum size of an interval covering q_val.
            if active_intervals_heap:
                min_size, _ = active_intervals_heap[0]  # Get size from (size, right_endpoint)
                ans[original_idx] = min_size
            # If heap is empty, no interval covers q_val, ans[original_idx] remains -1 (its initial value).

        return ans
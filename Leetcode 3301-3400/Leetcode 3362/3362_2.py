# Leetcode 3362: Zero Array transformation III
# https://leetcode.com/problems/zero-array-transformation-iii/
# Solved on 22nd of May, 2025
import heapq


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Given an array nums and a list of queries, where each query [l, r]
        represents an operation that can be applied to increment nums[i] by 1
        for all i in the range [l, r]. The goal is to make all elements in nums
        zero by applying a subset of the queries. We want to maximize the number
        of queries that are *not* used.

        This problem can be framed as a minimum cost maximum flow problem, but
        a greedy approach using a difference array and a min-heap (simulated
        with a max-heap of negated values) is more efficient.

        Args:
            nums: The input array of integers.
            queries: A list of queries, where each query is [l, r].

        Returns:
            The maximum number of queries that can be removed while still being
            able to make all elements in nums zero. Returns -1 if it's impossible
            to make all elements zero.
        """
        n = len(nums)
        total_queries = len(queries)

        # Difference array to keep track of current coverages
        diff = [0] * (n + 1)
        current_extra = 0
        chosen = 0

        # Sort queries based on their start indices
        queries_sorted = sorted(queries, key=lambda x: x[0])

        heap = []   # Max-heap to store the right endpoints of queries
        j = 0   # Pointer for queries_sorted

        for i in range(n):
            if i > 0:
                current_extra += diff[i]    # Update current coverage

            # Push queries that can currently be used (start at or before i)
            while j < len(queries_sorted) and queries_sorted[j][0] <= i:
                heapq.heappush(heap, -queries_sorted[j][1])     # Use negate for max-heap
                j += 1

            # Determine how much coverage is still needed
            required = nums[i] - current_extra
            while required > 0:
                # Remove queries from heap that do not cover index i
                while heap and -heap[0] < i:
                    heapq.heappop(heap)
                if not heap:    # Not enough queries to cover
                    return -1
                best_r = -heapq.heappop(heap)   # Choose the furthest reaching query
                chosen += 1
                # Apply this query's effect using the difference array
                diff[i] += 1
                if best_r + 1 < len(diff):
                    diff[best_r + 1] -= 1
                current_extra += 1  # Immediate effect at index i
                required -= 1   # Decrease the requirement

        return total_queries - chosen   # Total queries minus the chosen ones
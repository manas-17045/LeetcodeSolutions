# Leetcode 3488: Closest Equal Element Queries
# https://leetcode.com/problems/closest-equal-element-queries/
# Solved on 14th of October, 2025
class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        For each query index, find the minimum circular distance to another element with the same value.
        If no other element with the same value exists, the distance is -1.

        Args:
            nums: A list of integers representing the circular array.
            queries: A list of integer indices to query.
        Returns:
            A list of integers, where each element is the minimum circular distance for the corresponding query.
        """
        n = len(nums)
        # Map each value -> list of indices where it appears (in increasing order)
        positions = {}
        for i, v in enumerate(nums):
            positions.setdefault(v, []).append(i)

        # Precompute answer (minimum circular distance to another equal element) for every index
        min_dist = [-1] * n
        for v, idxs in positions.items():
            k = len(idxs)
            if k <= 1:
                # unique value -> no other equal element
                continue
            # idxs are already in ascending order because we appended in index order
            for j in range(k):
                cur = idxs[j]
                prev = idxs[j - 1]  # previous occurrence (wraps when j == 0)
                nxt = idxs[(j + 1) % k]  # next occurrence (wraps to first when j == k-1)

                # circular distances: positive modulo n
                d_prev = (cur - prev) % n
                d_next = (nxt - cur) % n

                # Nearest equal element is the closer of the two neighbors along the circle
                min_dist[cur] = d_prev if d_prev < d_next else d_next

        # Answer queries
        return [min_dist[q] for q in queries]
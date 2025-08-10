# Leetcode 1439: Find the Kth Smallest Sum of a Matrix With Sorted Rows
# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
# Solved on 10th of August, 2025
import heapq


class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        """
        Finds the k-th smallest sum among all possible sums formed by picking one element from each row.

        Args:
            mat: A list of lists of integers representing the matrix. Each row is sorted in non-decreasing order.
            k: The k-th smallest sum to find.
        Returns:
            The k-th smallest sum.
        """

        # Start with a single sum 0
        cur_sums = [0]

        for row in mat:
            # Only the first k elements of a sorted row can contribute to the k smallest sum
            row = row[:k]
            heap = []
            for i, s in enumerate(cur_sums):
                heapq.heappush(heap, (s + row[0], i, 0))

            new_sums = []
            # Extract up to k smallest combined sums
            limit = min(k, len(cur_sums) * len(row))
            for _ in range(limit):
                total, i, j = heapq.heappop(heap)
                new_sums.append(total)
                # try to advance in the row for this cur_sums index
                if j + 1 < len(row):
                    heapq.heappush(heap, (cur_sums[i] + row[j + 1], i, j + 1))

            cur_sums = new_sums

        return cur_sums[k - 1]
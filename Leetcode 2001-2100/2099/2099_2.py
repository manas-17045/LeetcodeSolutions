# Leetcode 2099: Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# Solved on 28th of June, 2025
import heapq


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """
        Given an integer array nums and an integer k, return the subsequence of nums of length k that has the largest sum.
        A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

        The solution finds the k largest elements by value and then reconstructs the subsequence while preserving their original relative order.
        It uses a min-heap to efficiently keep track of the k largest elements encountered so far.
        """
        # Find the indices of the k largest elements by value.
        heap = []
        for idx, val in enumerate(nums):
            if len(heap) < k:
                heapq.heappush(heap, (val, idx))
            else:
                # If current val is bigger than the smallest in heap, replace it.
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, idx))

        # Sort the k elements of heap by original index to preserve order.
        top_k = sorted(heap, key=lambda x: x[1])

        # Return just the values in that order.
        return [val for val, _ in top_k]
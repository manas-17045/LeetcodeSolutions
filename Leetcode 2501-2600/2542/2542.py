# Leetcode 2542: Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/
# Solved on 19th of November, 2025
import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Calculates the maximum score achievable from a subsequence of length k.

        The score of a subsequence is defined as the sum of its elements from nums1
        multiplied by the minimum of its elements from nums2.

        Args:
            nums1: A list of integers.
            nums2: A list of integers of the same length as nums1.
            k: The desired length of the subsequence.

        Returns:
            The maximum possible score.
        """
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        minHeap = []
        currentSum = 0
        result = 0

        for val1, val2 in pairs:
            heapq.heappush(minHeap, val1)
            currentSum += val1

            if len(minHeap) > k:
                currentSum -= heapq.heappop(minHeap)

            if len(minHeap) == k:
                result = max(result, currentSum * val2)

        return result
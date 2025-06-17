# Leetcode 2386: Find the K-Sum of an Array
# https://leetcode.com/problems/find-the-k-sum-of-an-array/
# Solved on 16th of June, 2025
import heapq


class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        """
        Finds the k-th largest sum of a subsequence of `nums`.

        The approach is to first calculate the maximum possible sum by taking all
        positive numbers. Then, we transform the problem into finding the k-th
        smallest "cost" to subtract from this maximum sum. The costs are the
        absolute values of the numbers in `nums`. We use a min-heap to efficiently
        explore the smallest costs.

        Args:
            nums: A list of integers.
            k: The rank of the sum to find (1-indexed).

        Returns:
            The k-th largest sum of a subsequence of `nums`.
        """
        n = len(nums)
        maxSum = 0
        for i in range(n):
            if nums[i] > 0:
                maxSum += nums[i]
            else:
                nums[i] = -nums[i]

        absNums = sorted(nums)

        kthSmallestDeviation = 0
        pq = [(0, 0)]

        for _ in range(k):
            s, i = heapq.heappop(pq)
            kthSmallestDeviation = s
            if i < n:
                heapq.heappush(pq, (s + absNums[i], (i + 1)))
                if i > 0:
                    heapq.heappush(pq, (s - absNums[i - 1] + absNums[i], (i + 1)))

        return maxSum - kthSmallestDeviation
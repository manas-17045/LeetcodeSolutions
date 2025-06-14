# Leetcode 2163: Minimum Difference in Sums After Removal of Elements
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
# Solved on 14th of June, 2025
import heapq


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        """
        Calculates the minimum difference between the sum of the first n elements
        and the sum of the last n elements after removing n elements from the middle.

        The problem requires dividing the input array `nums` of length 3n into three
        subarrays of length n. We need to remove n elements from the middle part
        such that the difference between the sum of the first n elements and the
        sum of the last n elements is minimized.

        Args:
            nums: A list of integers of length 3n.
        """
        n = len(nums) // 3

        prefixMinSums = [0] * (3 * n)
        maxHeap = []
        currentSum = 0
        for i in range(2 * n):
            heapq.heappush(maxHeap, -nums[i])
            currentSum += nums[i]
            if len(maxHeap) > n:
                removed = -heapq.heappop(maxHeap)
                currentSum -= removed
            if len(maxHeap) == n:
                prefixMinSums[i] = currentSum

        suffixMaxSums = [0] * (3 * n)
        minHeap = []
        currentSum = 0
        for i in range(3 * (n - 1), (n - 1), -1):
            heapq.heappush(minHeap, nums[i])
            currentSum += nums[i]
            if len(minHeap) > n:
                removed = heapq.heappop(minHeap)
                currentSum -= removed
            if len(minHeap) == n:
                suffixMaxSums[i] = currentSum

        minDifference = float('inf')

        for i in range((n - 1), 2 * n):
            sumFirst = prefixMinSums[i]
            sumSecond = suffixMaxSums[i + 1]
            minDifference = min(minDifference, (sumFirst - sumSecond))

        return minDifference
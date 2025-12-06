# Leetcode 3578: Count Partitions With Max-Min Difference at Most K
# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/
# Solved on 6th of November, 2025
from collections import deque


class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        """
        Counts the number of ways to partition the array `nums` such that for each partition,
        the difference between its maximum and minimum element is at most `k`.
        :param nums: A list of integers.
        :param k: An integer representing the maximum allowed difference between max and min in a partition.
        :return: The number of valid partitions modulo 10^9 + 7.
        """
        n = len(nums)
        mod = 10 ** 9 + 7

        prefixSum = [0] * (n + 2)
        prefixSum[1] = 1

        maxDeque = deque()
        minDeque = deque()
        left = 0

        currentWays = 0

        for right in range(n):
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)

            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)

            while nums[maxDeque[0]] - nums[minDeque[0]] > k:
                left += 1
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()

            currentWays = (prefixSum[right + 1] - prefixSum[left]) % mod
            prefixSum[right + 2] = (prefixSum[right + 1] + currentWays) % mod

        return currentWays
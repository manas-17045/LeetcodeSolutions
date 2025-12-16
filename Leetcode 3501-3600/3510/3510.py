# Leetcode 3510: Minimum Pair Removal to Sort Array II
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
# Solved on 16th of December, 2025
import heapq


class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of pair removals required to sort the array.

        Args:
            nums: A list of integers representing the input array.

        Returns:
            The minimum number of pair removals needed to sort the array.
        """
        n = len(nums)
        if n <= 1:
            return 0

        val = list(nums)
        nextIndices = [0] * n
        prevIndices = [0] * n
        removed = [False] * n

        for i in range(n):
            nextIndices[i] = -1 if i == n - 1 else i + 1
            prevIndices[i] = -1 if i == 0 else i - 1

        badCount = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                badCount += 1

        if badCount == 0:
            return 0

        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (val[i] + val[i + 1], i, i + 1))

        ops = 0

        while badCount > 0 and pq:
            currSum, u, v = heapq.heappop(pq)

            if removed[u] or nextIndices[u] != v or val[u] + val[v] != currSum:
                continue

            ops += 1
            h = prevIndices[u]
            w = nextIndices[v]

            if val[u] > val[v]:
                badCount -= 1
            if h != -1 and val[h] > val[u]:
                badCount -= 1
            if w != -1 and val[v] > val[w]:
                badCount -= 1

            val[u] += val[v]
            removed[v] = True
            nextIndices[u] = w

            if w != -1:
                prevIndices[w] = u

            if h != -1:
                if val[h] > val[u]:
                    badCount += 1
                heapq.heappush(pq, (val[h] + val[u], h, u))

            if w != -1:
                if val[u] > val[w]:
                    badCount += 1
                heapq.heappush(pq, (val[u] + val[w], u, w))

        return ops
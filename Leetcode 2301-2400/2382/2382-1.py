# Leetcode 2382: Maximum Segment Sum After Removals
# https://leetcode.com/problems/maximum-segment-sum-after-removals/
# Solved on 26th of August, 2025
class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        """
        Calculates the maximum segment sum after each removal query.

        Args:
            nums: A list of integers representing the initial array.
            removeQueries: A list of integers representing the indices to be removed.

        Returns:
            A list of integers, where each element is the maximum segment sum after the corresponding removal query.
        """
        n = len(nums)
        parent = list(range(n))
        segmentSum = [0] * n
        exists = [False] * n

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parent[rootI] = rootJ
                segmentSum[rootJ] += segmentSum[rootI]

        ans = [0] * n
        maxSum = 0

        for i in range(n - 1, -1, -1):
            ans[i] = maxSum

            queryIndex = removeQueries[i]

            exists[queryIndex] = True
            segmentSum[queryIndex] = nums[queryIndex]

            if queryIndex > 0 and exists[queryIndex - 1]:
                union(queryIndex, queryIndex - 1)

            if queryIndex < n - 1 and exists[queryIndex + 1]:
                union(queryIndex, queryIndex + 1)

            finalRoot = find(queryIndex)
            maxSum = max(maxSum, segmentSum[finalRoot])

        return ans
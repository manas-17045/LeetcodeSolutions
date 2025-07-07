# Leetcode 2736: Maximum Sum Queries
# https://leetcode.com/problems/maximum-sum-queries/
# Solved on 7th of July, 2025
import bisect


class Solution:
    def maximumSumQueries(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        """
        Given two 0-indexed integer arrays nums1 and nums2 of length n, and two 0-indexed integer arrays queries of length m,
        where queries[i] = [xi, yi].

        For each query, you need to find the maximum sum nums1[j] + nums2[j] among all indices j such that nums1[j] >= xi and nums2[j] >= yi.
        If no such index j exists, the answer for this query is -1.

        Return an array answer of length m where answer[i] is the answer to the ith query.
        """
        n = len(nums1)
        q = len(queries)

        pairs = []
        for i in range(n):
            pairs.append((nums1[i], nums2[i]))

        pairs.sort(key=lambda p: p[0], reverse=True)

        indexedQueries = []
        for i in range(q):
            indexedQueries.append((queries[i][0] + queries[i][1], i))

        indexedQueries.sort(key=lambda query: query[0], reverse= True)

        answer = [-1] * q
        monotonicStack = []
        pairIndex = 0

        for queryX, queryY, originalIndex in indexedQueries:
            while pairIndex < n and pairs[pairIndex][0] >= queryX:
                currentNum1, currentNum2 = pairs[pairIndex]
                currentSum = currentNum1 + currentNum2

                while monotonicStack and monotonicStack[-1][1] <= currentSum:
                    monotonicStack.pop()

                if not monotonicStack or monotonicStack[-1][0] < currentNum2:
                    monotonicStack.append((currentNum2, currentSum))

                pairIndex += 1

            searchTuple = (queryY, 0)
            insertionPoint = bisect.bisect_left(monotonicStack, searchTuple)

            if insertionPoint < len(monotonicStack):
                answer[originalIndex] = monotonicStack[insertionPoint][1]

        return answer
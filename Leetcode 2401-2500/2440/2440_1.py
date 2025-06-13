# Leetcode 2440: Create Components With Same Value
# https://leetcode.com/problems/create-components-with-same-value/
# Solved on 13th of June, 2025
from collections import defaultdict


class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:
        """
        Given a tree represented by `nums` (node values) and `edges`, find the maximum number of edges
        that can be deleted such that the remaining connected components all have the same sum.

        Args:
            nums: A list of integers representing the values of the nodes.
            edges: A list of lists representing the edges of the tree.

        Returns:
            The maximum number of edges that can be deleted.
        """
        n = len(nums)
        if n <= 1:
            return 0

        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        totalSum = sum(nums)

        def dfs(u, p, target):
            sumAtNode = nums[u]
            for v in adjList[u]:
                if v == p:
                    continue
                sumFromChild = dfs(v, u, target)
                if sumFromChild == -1:
                    return -1
                sumAtNode += sumFromChild

            if sumAtNode > target:
                return -1
            if sumAtNode == target:
                return 0
            return sumAtNode

        divisors = []
        for i in range(1, int(totalSum**0.5) + 1):
            if totalSum % i == 0:
                divisors.append(i)
                if i * i != totalSum:
                    divisors.append(totalSum // i)

        maxDeletedEdges = 0
        for target in divisors:
            if target >= totalSum:
                continue

            if totalSum % target == 0:
                if dfs(0, -1, target) == 0:
                    componentCount = totalSum // target
                    deletedEdges = componentCount - 1
                    maxDeletedEdges = max(maxDeletedEdges, deletedEdges)


        return maxDeletedEdges
# Leetcode 3715: Sum of Perfect Square Ancestors
# https://leetcode.com/problems/sum-of-perfect-square-ancestors/
# Solved on 21st of December, 2025
import sys
from collections import defaultdict
sys.setrecursionlimit(200000)


class Solution:
    def sumOfAncestors(self, n: int, edges: list[list[int]], nums: list[int]) -> int:
        """
        Calculates the sum of perfect square ancestors for each node in a tree.
        :param n: The number of nodes in the tree.
        :param edges: A list of lists representing the edges of the tree.
        :param nums: A list of integers where nums[i] is the value of node i.
        :return: The total sum of perfect square ancestors.
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        maxVal = max(nums)
        squareFree = list(range(maxVal + 1))

        for i in range(2, int(maxVal ** 0.5) + 1):
            sq = i * i
            for j in range(sq, maxVal + 1, sq):
                while squareFree[j] % sq == 0:
                    squareFree[j] //= sq

        ancestorCounts = defaultdict(int)
        totalSum = 0

        def dfs(node, parent):
            nonlocal totalSum
            val = nums[node]
            sfp = squareFree[val]

            totalSum += ancestorCounts[sfp]

            ancestorCounts[sfp] += 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
            ancestorCounts[sfp] -= 1

        dfs(0, -1)
        return totalSum
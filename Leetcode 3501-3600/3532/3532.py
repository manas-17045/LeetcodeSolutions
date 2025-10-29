# Leetcode 3532: Path Existence Queries in a Graph I
# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
# Solved on 29th of October, 2025
class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        """
        Determines if a path exists between two nodes in a graph based on a maximum difference constraint.

        Args:
            n (int): The number of nodes in the graph.
            nums (list[int]): A list of values associated with each node.
            maxDiff (int): The maximum allowed difference between values of adjacent nodes in a path.
            queries (list[list[int]]): A list of queries, where each query is a pair of node indices [node1, node2].

        Returns:
            list[bool]: A list of booleans, where each boolean indicates whether a path exists for the corresponding query.
        """

        nodeComponent = [0] * n
        componentIndex = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                componentIndex += 1
            nodeComponent[i] = componentIndex

        result = []
        for q in queries:
            nodeOne = q[0]
            nodeTwo = q[1]

            isSameComponent = (nodeComponent[nodeOne] == nodeComponent[nodeTwo])
            result.append(isSameComponent)

        return result
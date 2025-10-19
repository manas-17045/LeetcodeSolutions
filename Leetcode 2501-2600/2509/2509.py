# Leetcode 2509: Cycle Length Queries in a Tree
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/
# Solved on 19th of October, 2025
class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        Calculates the length of the cycle formed by adding an edge between two nodes in a complete binary tree.

        The tree is represented such that the root is node 1, and for any node i, its left child is 2*i
        and its right child is 2*i + 1.

        Args:
            n (int): The number of levels in the complete binary tree (not directly used in the logic, but defines the tree size).
            queries (list[list[int]]): A list of queries, where each query is a list [nodeA, nodeB] representing two nodes.

        Returns:
            list[int]: A list of integers, where each integer is the cycle length for the corresponding query.
        """
        results = []

        for query in queries:
            nodeA = query[0]
            nodeB = query[1]

            pathLength = 0

            while nodeA != nodeB:
                if nodeA > nodeB:
                    nodeA //= 2
                else:
                    nodeB //= 2
                pathLength += 1

            results.append(pathLength + 1)

        return results
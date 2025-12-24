# Leetcode 3786: Total Sum of Interaction Cost in Tree Groups
# https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/
# Solved on 24th of December, 2025
class Solution:
    def interactionCost(self, n: int, edges: list[list[int]], group: list[int]) -> int:
        """
        Calculates the total sum of interaction costs in tree groups.

        Args:
            n: The number of nodes in the tree.
            edges: A list of lists representing the edges of the tree.
            group: A list where group[i] is the group ID of node i.

        Returns:
            The total sum of interaction costs.
        """

        if n == 1:
            return 0

        adjacencyList = [[] for _ in range(n)]
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        groupCounts = [0] * 21
        for g in group:
            groupCounts[g] += 1

        parent = [-1] * n
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)
            for v in adjacencyList[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)

        subtreeCounts = [[0] * 21 for _ in range(n)]
        totalInteractionCost = 0

        for i in range(n - 1, -1, -1):
            u = order[i]
            currentGroup = group[u]
            subtreeCounts[u][currentGroup] += 1

            for v in adjacencyList[u]:
                if v == parent[u]:
                    continue

                for groupIndex in range(1, 21):
                    countInSubtree = subtreeCounts[v][groupIndex]
                    if countInSubtree > 0:
                        countOutside = groupCounts[groupIndex] - countInSubtree
                        totalInteractionCost += countInSubtree * countOutside
                        subtreeCounts[u][groupIndex] += countInSubtree

        return totalInteractionCost
# Leetcode 2508: Add Edges to Make Degrees of All Nodes Even
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/
# Solved on 20th of November, 2025
class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        """
        Determines if it's possible to make the degrees of all nodes even by adding at most two edges.
        :param n: The number of nodes in the graph.
        :param edges: A list of edges in the graph.
        :return: True if it's possible to make all degrees even, False otherwise.
        """
        adjList = [set() for _ in range(n + 1)]
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        oddNodes = []
        for i in range(1, n + 1):
            if len(adjList[i]) % 2 == 1:
                oddNodes.append(i)

        oddCount = len(oddNodes)

        if oddCount == 0:
            return True

        if oddCount == 2:
            node1 = oddNodes[0]
            node2 = oddNodes[1]
            if node2 not in adjList[node1]:
                return True
            for i in range(1, n + 1):
                if i != node1 and i != node2 and i not in adjList[node1] and i not in adjList[node2]:
                    return True
            return False

        if oddCount == 4:
            a = oddNodes[0]
            b = oddNodes[1]
            c = oddNodes[2]
            d = oddNodes[3]
            if b not in adjList[a] and d not in adjList[c]:
                return True
            if c not in adjList[a] and d not in adjList[b]:
                return True
            if d not in adjList[a] and c not in adjList[b]:
                return True
            return False

        return False
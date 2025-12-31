# Leetcode 3419: Minimize the Maximum Edge Weight of Graph
# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/
# Solved on 31st of December, 2025
class Solution:
    def minMaxWeight(self, n: int, edges: list[list[int]], threshold: int) -> int:
        """
        Minimizes the maximum edge weight of a graph such that all nodes are reachable from node 0
        using only edges with weight less than or equal to the chosen maximum, and the total
        number of such edges used is within a given threshold.

        :param n: The number of nodes in the graph.
        :param edges: A list of edges, where each edge is represented as [u, v, w] (u -> v with weight w).
        :param threshold: The maximum allowed number of edges in the path. (Note: This parameter seems unused in the provided code snippet,
                          but is part of the problem statement context).
        :return: The minimum possible maximum edge weight that satisfies the conditions.
        """
        reversedGraph = [[] for _ in range(n)]
        uniqueWeights = set()

        for u, v, w in edges:
            reversedGraph[v].append((u, w))
            uniqueWeights.add(w)

        sortedWeights = sorted(list(uniqueWeights))

        def isFeasible(maxW):
            visited = [False] * n
            visited[0] = True
            stack = [0]
            count = 1

            while stack:
                u = stack.pop()
                for v, w in reversedGraph[u]:
                    if w <= maxW and not visited[v]:
                        visited[v] = True
                        count += 1
                        stack.append(v)

            return count == n

        left, right = 0, len(sortedWeights) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            currentW = sortedWeights[mid]
            if isFeasible(currentW):
                ans = currentW
                right = mid - 1
            else:
                left = mid + 1

        return ans
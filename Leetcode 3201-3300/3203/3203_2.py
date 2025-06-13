# Leetcode 3203: Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees
# Solved on 13th of June, 2025
from collections import defaultdict, deque


class Solution:
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        """
        Calculates the minimum possible diameter of a new tree formed by merging two given trees.
        The merge operation involves adding an edge between any node from the first tree and any node from the second tree.

        Args:
            edges1: A list of edges representing the first tree.
            edges2: A list of edges representing the second tree.

        Returns:
            The minimum possible diameter of the merged tree.
        """
        def getTreeProperties(edges: list[list[int]]):
            numNodes = len(edges) + 1
            if numNodes == 1:
                return 0, 0

            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            def bfs(startNode):
                distances = [-1] * numNodes
                distances[startNode] = 0
                queue = deque([startNode])

                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if distances[v] == -1:
                            distances[v] = distances[u] + 1
                            queue.append(v)

                maxDist = -1
                farthestNode = -1
                for i in range(numNodes):
                    if distances[i] > maxDist:
                        maxDist = distances[i]
                        farthestNode = i

                return distances, farthestNode

            _, a = bfs(0)
            distFromA, b = bfs(a)
            diameter = distFromA[b]

            distFromB, _ = bfs(b)

            minEccentricity = float('inf')
            for i in range(numNodes):
                eccentricity = max(distFromA[i], distFromB[i])
                minEccentricity = min(minEccentricity, eccentricity)

            return diameter, minEccentricity

        diam1, minEcc1 = getTreeProperties(edges1)
        diam2, minEcc2 = getTreeProperties(edges2)

        longestPathThroughBridge = minEcc1 + minEcc2 + 1

        return max(diam1, diam2, longestPathThroughBridge)
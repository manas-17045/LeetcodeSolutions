# Leetcode 2203: Minimum Weighted Subgraph With the Required Paths
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
# Solved on 14th of September, 2025
import heapq


class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        """
        Finds the minimum weighted subgraph such that there are paths from src1 to some node,
        from src2 to the same node, and from that node to dest.
        :param n: The number of nodes in the graph.
        :param edges: A list of edges, where each edge is [u, v, w] representing a directed edge
                      from u to v with weight w.
        :param src1: The first source node.
        :param src2: The second source node.
        :param dest: The destination node.
        :return: The minimum total weight of such a subgraph, or -1 if no such subgraph exists.
        """
        graph = [[] for _ in range(n)]
        reversedGraph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            reversedGraph[v].append((u, w))

        def runDijkstra(startNode, adjList):
            distances = [float('inf')] * n
            distances[startNode] = 0
            priorityQueue = [(0, startNode)]

            while priorityQueue:
                dist, node = heapq.heappop(priorityQueue)

                if dist > distances[node]:
                    continue

                for neighbor, weight in adjList[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
                        heapq.heappush(priorityQueue, (distances[neighbor], neighbor))

            return distances

        distFromSrc1 = runDijkstra(src1, graph)
        distFromSrc2 = runDijkstra(src2, graph)
        distToDest = runDijkstra(dest, reversedGraph)

        minWeight = float('inf')
        for i in range(n):
            path1 = distFromSrc1[i]
            path2 = distFromSrc2[i]
            path3 = distToDest[i]

            if path1 != float('inf') and path2 != float('inf') and path3 != float('inf'):
                currentWeight = path1 + path2 + path3
                minWeight = min(minWeight, currentWeight)

        return minWeight if minWeight != float('inf') else -1
# Leetcode 882: Reachable Nodes In Subdivided Graph
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
# Solved on 7th of August, 2025
import collections
import heapq


class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        """
        Calculates the number of reachable nodes in a subdivided graph.

        Args:
            edges: A list of edges, where each edge is a list [u, v, cnt]
                   representing an edge between nodes u and v with cnt new nodes
                   inserted.
            maxMoves: The maximum number of moves allowed.
            n: The total number of original nodes.

        Returns:
            The total number of reachable nodes.
        """
        graph = collections.defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))

        distances = [float('inf')] * n
        distances[0] = 0
        priorityQueue = [(0, 0)]  # (distance, node)

        while priorityQueue:
            currentDistance, currentNode = heapq.heappop(priorityQueue)

            if currentDistance > distances[currentNode]:
                continue

            for neighborNode, weight in graph[currentNode]:
                newDistance = currentDistance + weight
                if newDistance < distances[neighborNode]:
                    distances[neighborNode] = newDistance
                    heapq.heappush(priorityQueue, (newDistance, neighborNode))
        
        totalReachableNodes = 0
        
        for i in range(n):
            if distances[i] <= maxMoves:
                totalReachableNodes += 1
                
        for u, v, cnt in edges:
            reachableFromU = 0
            if distances[u] <= maxMoves:
                reachableFromU = maxMoves - distances[u]
            
            reachableFromV = 0
            if distances[v] <= maxMoves:
                reachableFromV = maxMoves - distances[v]
            
            reachableOnEdge = min(cnt, reachableFromU + reachableFromV)
            totalReachableNodes += reachableOnEdge
            
        return totalReachableNodes
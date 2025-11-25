# Leetcode 3620: Network Recovery Pathways
# https://leetcode.com/problems/network-recovery-pathways/
# Solved on 25th of November, 2025
import collections


class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        """
        Finds the maximum path score such that there exists a path from node 0 to node n-1
        with a total weight less than or equal to k, and all nodes on the path are online.
        The path score is defined as the minimum edge weight along the path.

        Args:
            edges: A list of lists, where each inner list represents an edge [u, v, w],
                   meaning there's a directed edge from node u to node v with weight w.
            online: A list of booleans, where online[i] is True if node i is online, False otherwise.
            k: The maximum allowed total weight of the path.

        Returns:
            The maximum possible path score. Returns -1 if no such path exists.
        """
        n = len(online)
        adj = [[] for _ in range(n)]
        inDegree = [0] * n
        uniqueWeights = set()

        for u, v, w in edges:
            adj[u].append((v, w))
            inDegree[v] += 1
            uniqueWeights.add(w)

        sortedWeights = sorted(list(uniqueWeights))

        topoOrder = []
        queue = collections.deque([i for i in range(n) if inDegree[i] == 0])

        while queue:
            u = queue.popleft()
            topoOrder.append(u)
            for v, w in adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)

        low = 0
        high = len(sortedWeights) - 1
        maxScore = -1

        while low <= high:
            mid = (low + high) // 2
            currentMin = sortedWeights[mid]

            minCost = [float('inf')] * n
            minCost[0] = 0

            for u in topoOrder:
                if minCost[u] == float('inf') or not online[u]:
                    continue

                if minCost[u] > k:
                    continue

                for v, w in adj[u]:
                    if w >= currentMin and online[v]:
                        newCost = minCost[u] + w
                        if newCost < minCost[v]:
                            minCost[v] = newCost

            if minCost[n - 1] <= k:
                maxScore = currentMin
                low = mid + 1
            else:
                high = mid - 1

        return maxScore
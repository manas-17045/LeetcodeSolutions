# Leetcode 3924: Minimum Threshold Path With Limited Heavy Edges
# https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/
# Solved on 23rd of May, 2026
import collections


class Solution:
    def minimumThreshold(self, n: int, edges: list[list[int]], source: int, target: int, k: int) -> int:
        """
        Finds the minimum threshold value such that there exists a path from source to target
        with at most k edges having a weight greater than the threshold.

        :param n: Number of nodes in the graph.
        :param edges: List of edges where each edge is [u, v, w].
        :param source: Starting node.
        :param target: Destination node.
        :param k: Maximum allowed number of heavy edges (weight > threshold).
        :return: The minimum threshold value.
        """
        graph = [[] for _ in range(n)]
        maxWeight = 0
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            if w > maxWeight:
                maxWeight = w

        def isValid(mid: int) -> bool:
            minHeavy = [float('inf')] * n
            minHeavy[source] = 0
            dq = collections.deque([source])

            while dq:
                curr = dq.popleft()

                if curr == target:
                    return minHeavy[target] <= k

                if minHeavy[curr] > k:
                    continue

                for adj, weight in graph[curr]:
                    cost = 1 if weight > mid else 0
                    if minHeavy[curr] + cost < minHeavy[adj]:
                        minHeavy[adj] = minHeavy[curr] + cost
                        if cost == 0:
                            dq.appendleft(adj)
                        else:
                            dq.append(adj)

            return minHeavy[target] <= k

        left = 0
        right = maxWeight
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
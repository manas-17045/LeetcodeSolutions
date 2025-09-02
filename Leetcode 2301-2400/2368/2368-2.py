# Leetcode 2368: Reachable Nodes With Restrictions
# https://leetcode.com/problems/reachable-nodes-with-restrictions/
# Solved on 2nd of September, 2025
import collections


class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        """
        Calculates the number of reachable nodes starting from node 0,
        avoiding restricted nodes.
        :param n: The total number of nodes in the graph.
        :param edges: A list of lists representing the edges in the graph.
        :param restricted: A list of nodes that cannot be visited.
        :return: The total count of reachable nodes.
        """
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # mark restricted nodes
        is_restricted = [False] * n
        for r in restricted:
            if 0 <= r < n:
                is_restricted[r] = True

        # BFS from node 0
        visited = [False] * n
        q = collections.deque()
        visited[0] = True
        count = 0

        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                if not is_restricted[nei] and not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return count
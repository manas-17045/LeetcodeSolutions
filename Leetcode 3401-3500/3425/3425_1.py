# Leetcode 3425: Longest Special Path
# https://leetcode.com/problems/longest-special-path/
# Solved on 30th of June, 2025
from collections import defaultdict, deque
import sys
sys.setrecursionlimit(5 * 10**4 + 5)


class Solution:
    def longestSpecialPath(self, edges: list[list[int]], nums: list[int]) -> list[int]:
        """
        Finds the longest "special path" in a tree.

        A special path is a path from a node `u` to its ancestor `v` such that
        all nodes on the path (excluding `v`) have values `nums[x]` that have
        not appeared on the path from the root to `v`.

        Args:
            edges: A list of lists representing the tree edges. Each inner list
                   is [u, v, w], where u and v are nodes and w is the edge weight.
            nums: A list of integers where nums[i] is the value of node i.

        Returns:
            A list [maxLength, minNodes] representing the length of the longest
            special path and the minimum number of nodes in such a path.
        """
        n = len(nums)
        if n <= 1:
            return [0, n]

        maxLogN = n.bit_length()

        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        treeChildren = defaultdict(list)
        parent = [-1] * n
        depth = [-1] * n
        dist = [-1] * n

        queue = deque([(0, -1, 0, 0)])
        visited = {0}

        depth[0] = 0
        dist[0] = 0

        while queue:
            u, p, d, di = queue.popleft()
            parent[u] = p
            for v, w in adj[u]:
                if v != p:
                    visited.add(v)
                    depth[v] = d + 1
                    dist[v] = di + w
                    treeChildren[u].append(v)
                    queue.append((v, u, d + 1, di + w))

        up = [[-1] * maxLogN for _ in range(n)]
        for i in range(n):
            up[i][0] = parent[i]

        for j in range(1, maxLogN):
            for i in range(n):
                if up[i][j - 1] != -1:
                    up[i][j] = up[up[i][j - 1]][j - 1]

        def getKthAncestor(u, k):
            if k < 0:
                return -1
            for j in range(maxLogN -1, -1, -1):
                if (k >> j) & 1:
                    if u == -1:
                        return -1
                    u = up[u][j]
            return u

        self.maxLength = 0
        self.minNodes = 1

        def dfs(u, valToNode, maxConflictDepth):
            valU = nums[u]
            conflictNode = valToNode.get(valU, -1)

            conflictDepth = -1
            if conflictNode != -1:
                conflictDepth = depth[conflictNode]

            currentMaxConflictDepth = max(maxConflictDepth, conflictDepth)

            startNodeDepth = currentMaxConflictDepth + 1
            k = depth[u] - startNodeDepth
            startNode = getKthAncestor(u, k)

            if startNode != -1:
                pathLen = dist[u] - dist[startNode]
                pathNodes = depth[u] - depth[startNode] + 1

                if pathLen > self.maxLength:
                    self.maxLength = pathLen
                    self.minNodes = pathNodes
                elif pathLen == self.maxLength:
                    self.minNodes = min(self.minNodes, pathNodes)

            oldNodeForVal = valToNode.get(valU)
            valToNode[valU] = u

            for v in treeChildren[u]:
                dfs(v, valToNode, currentMaxConflictDepth)

            if oldNodeForVal is None:
                del valToNode[valU]
            else:
                valToNode[valU] = oldNodeForVal

        dfs(0, {}, -1)

        return [self.maxLength, self.minNodes]
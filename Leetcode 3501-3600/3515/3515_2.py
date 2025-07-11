# Leetcode 3515: Shortest Path in a Weighted Tree
# https://leetcode.com/problems/shortest-path-in-a-weighted-tree/
# Solved on 11th of July, 2025
class Solution:
    def treeQueries(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        This function processes a series of queries on a tree structure where edge weights can be updated.
        It uses a Lazy Segment Tree to efficiently handle path sum queries (distance from root) and edge weight updates.

        Args:
            n (int): The number of nodes in the tree. Nodes are 1-indexed.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing an edge
                                     between node u and node v with weight w.
            queries (list[list[int]]): A list of queries. Each query is either:
                                       - [1, u, v, newWeight]: Update the weight of the edge between u and v to newWeight.
                                       - [2, x]: Query the distance from the root (node 1) to node x.

        Returns:
            list[int]: A list of answers for all type 2 queries in the order they appear.
        """
        tree = LazySegmentTree(n)
        ans = []
        graph = [[] for _ in range(n + 1)]
        edgeWeights = {}

        for edge in edges:
            u, v, w = edge[0], edge[1], edge[2]
            graph[u].append(v)
            graph[v].append(u)
            edgeWeights[(min(u, v), max(u, v))] = w

        inTime = [0] * (n + 1)
        outTime = [0] * (n + 1)
        dist = [0] * (n + 1)
        parent = [-1] * (n + 1)
        time = 0

        self.dfs(graph, 1, -1, time, inTime, outTime, dist, parent)

        for i in range(1, (n + 1)):
            tree.addRange(inTime[i], inTime[i], dist[i])

        for query in queries:
            queryType = query[0]
            if queryType == 1:
                u, v, newWeight = query[1], query[2], query[3]
                key = (min(u, v), max(u, v))
                oldWeight = edgeWeights[key]
                delta = newWeight - oldWeight
                edgeWeights[key] = newWeight
                child = v if parent[v] == u else u
                tree.addRange(inTime[child], outTime[child], delta)
            else:
                x = query[1]
                ans.append(tree.query(inTime[x]))

        return ans

class LazySegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def push(self, treeIndex, lo, hi):
        if self.lazy[treeIndex] == 0:
            return
        self.tree[treeIndex] += self.lazy[treeIndex]
        if lo != hi:
            self.lazy[2 * treeIndex + 1] += self.lazy[treeIndex]
            self.lazy[2 * treeIndex + 2] += self.lazy[treeIndex]
        self.lazy[treeIndex] = 0

    def addRange(self, l, r, val):
        self.addRangeHelper(0, 0, self.n - 1, l, r, val)

    def addRangeHelper(self, treeIndex, lo, hi, l, r, val):
        self.push(treeIndex, lo, hi)
        if r < lo or l > hi:
            return
        if l <= lo and hi <= r:
            self.lazy[treeIndex] += val
            self.push(treeIndex, lo, hi)
            return
        mid = (lo + hi) // 2
        self.addRangeHelper(2 * treeIndex + 1, lo, mid, l, r, val)
        self.addRangeHelper(2 * treeIndex + 2, mid + 1, hi, l, r, val)

    def query(self, i):
        return self.queryHelper(0, 0, self.n - 1, i)

    def queryHelper(self, treeIndex, lo, hi, i):
        self.push(treeIndex, lo, hi)
        if lo == hi:
            return self.tree[treeIndex]
        mid = (lo + hi) // 2
        if i <= mid:
            return self.queryHelper(2 * treeIndex + 1, lo, mid, i)
        return self.queryHelper(2 * treeIndex + 2, mid + 1, hi, i)
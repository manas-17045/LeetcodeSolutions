# Leetcode 3515: Shortest Path in a Weighted Tree
# https://leetcode.com/problems/shortest-path-in-a-weighted-tree/
# Solved on 11th of July, 2025
import sys
sys.setrecursionlimit(2 * 10**5)


class Solution:
    def treeQueries(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Solves the Shortest Path in a Weighted Tree problem using Heavy-Light Decomposition (HLD)
        and a Segment Tree.

        The problem involves a tree with weighted edges and two types of queries:
        1. Update the weight of an edge.
        2. Find the shortest path from the root (node 0) to a given target node.

        Args:
            n (int): The number of nodes in the tree.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing
                                     an edge between node u and node v with weight w.
            queries (list[list[int]]): A list of queries.
        """
        self.adjacencyList = [[] for _ in range(n)]
        for u, v, w in edges:
            u, v = (u - 1), (v - 1)
            self.adjacencyList[u].append((v, w))
            self.adjacencyList[v].append((u, w))

        self.parent = [-1] * n
        self.depth = [-1] * n
        self.subtreeSize = [0] * n
        self.heavyChild = [-1] * n
        self.edgeWeight = [0] * n

        self.dfs1(0, -1, 0)

        self.chainHead = [-1] * n
        self.position = [-1] * n
        self.positionCounter = 0
        self.dfs2(0, 0)

        baseArray = [0] * n
        for i in range(n):
            baseArray[self.position[i]] = self.edgeWeight[i]

        segmentTree = SegmentTree(baseArray)

        results = []
        for query in queries:
            queryType = query[0]
            if queryType == 1:
                u, v, newWeight = query[1] - 1, query[2] - 1, query[3]
                if self.parent[v] == u:
                    childNode = v
                else:
                    childNode = u
                segmentTree.updateValue(self.position[childNode], newWeight)
            else:
                targetNode = query[1] - 1
                totalDistance = 0
                currentNode = targetNode

                while currentNode != -1:
                    headOfCurrentPath = self.chainHead[currentNode]
                    totalDistance += segmentTree.querySum(self.position[headOfCurrentPath], self.position[currentNode])
                    currentNode = self.parent[headOfCurrentPath]

                results.append(totalDistance)

        return results

    def dfs1(self, u, p, d):
        self.parent[u] = p
        self.depth[u] = d
        self.subtreeSize[u] = 1
        maxSubtreeSize = 0

        for v, w in self.adjacencyList[u]:
            if v == p:
                continue
            self.edgeWeight = w
            self.dfs1(v, u, d + 1)
            self.subtreeSize[u] += self.subtreeSize[v]
            if self.subtreeSize[v] > maxSubtreeSize:
                maxSubtreeSize = self.subtreeSize[v]
                self.heavyChild[u] = v

    def dfs2(self, u, h):
        self.chainHead[u] = h
        self.position[u] = self.positionCounter
        self.positionCounter += 1

        if self.heavyChild[u] != -1:
            self.dfs2(self.heavyChild[u], h)

        for v, _ in self.adjacencyList[u]:
            if v != self.parent[u] and v != self.heavyChild[u]:
                self.dfs2(v, v)

class SegmentTree:
    def __init__(self, initialArray):
        self.size = len(initialArray)
        self.tree = [0] * (4 * self.size)
        self.array = initialArray
        if self.size > 0:
            self.build(0, 0, (self.size - 1))

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.array[start]
            return
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def updateValue(self, index, value):
        self._update(0, 0, self.size - 1, index, value)

    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if start <= index <= mid:
            self._update(2 * node + 1, start, mid, index, value)
        else:
            self._update(2 * node + 2, mid + 1, end, index, value)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def querySum(self, left, right):
        if left > right or self.size == 0:
            return 0
        return self._query(0, 0, self.size - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start and end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node + 1, start, mid, left, right)
        p2 = self._query(2 * node + 2, mid + 1, end, left, right)

        return p1 + p2
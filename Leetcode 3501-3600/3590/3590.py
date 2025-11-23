# Leetcode 3590: Kth Smallest Path XOR Sum
# https://leetcode.com/problems/kth-smallest-path-xor-sum/
# Solved on 23rd of November, 2025
import sys
sys.setrecursionlimit(200000)


class Solution:
    def kthSmallest(self, par: list[int], vals: list[int], queries: list[list[int]]) -> list[int]:
        """
        Finds the k-th smallest XOR sum from the root to a given node in a tree.
        :param par: A list representing the parent of each node. par[i] is the parent of node i. par[0] is -1.
        :param vals: A list representing the value of each node. vals[i] is the value of node i.
        :param queries: A list of queries, where each query is [u, k], asking for the k-th smallest XOR sum from root to node u.
        :return: A list of integers, where each element is the answer to the corresponding query.
        """
        n = len(par)
        adj = [[] for _ in range(n)]
        for i, p in enumerate(par):
            if p != -1:
                adj[p].append(i)

        pathXor = [0] * n
        pathXor[0] = vals[0]

        queue = [0]
        bfsOrder = []
        while queue:
            u = queue.pop(0)
            bfsOrder.append(u)
            for v in adj[u]:
                pathXor[v] = pathXor[u] ^ vals[v]
                queue.append(v)

        sz = [1] * n
        heavy = [-1] * n

        for i in range(n - 1, -1, -1):
            u = bfsOrder[i]
            maxSz = 0
            for v in adj[u]:
                sz[u] += sz[v]
                if sz[v] > maxSz:
                    maxSz = sz[v]
                    heavy[u] = v

        tour = []
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfsTour(u):
            nonlocal timer
            tin[u] = timer
            tour.append(u)
            timer += 1

            if heavy[u] != -1:
                dfsTour(heavy[u])

            for v in adj[u]:
                if v != heavy[u]:
                    dfsTour(v)

            tout[u] = timer - 1

        dfsTour(0)

        tourValues = [pathXor[node] for node in tour]

        nodeQueries = [[] for _ in range(n)]
        for idx, (u, k) in enumerate(queries):
            nodeQueries[u].append((k, idx))

        maxVal = 131072
        bit = [0] * (maxVal + 1)
        freq = [0] * maxVal
        distinctCount = 0

        def updateBit(idx, delta):
            idx += 1
            while idx <= maxVal:
                bit[idx] += delta
                idx += idx & (-idx)

        def queryKth(k):
            idx = 0
            currentSum = 0
            for i in range(17, -1, -1):
                nextIdx = idx + (1 << i)
                if nextIdx <= maxVal and currentSum + bit[nextIdx] < k:
                    idx = nextIdx
                    currentSum += bit[idx]
            return idx

        def add(val):
            nonlocal distinctCount
            if freq[val] == 0:
                updateBit(val, 1)
                distinctCount += 1
            freq[val] += 1

        def remove(val):
            nonlocal distinctCount
            freq[val] -= 1
            if freq[val] == 0:
                updateBit(val, -1)
                distinctCount -= 1

        ans = [0] * len(queries)

        def sack(u, keep):
            for v in adj[u]:
                if v != heavy[u]:
                    sack(v, False)

            if heavy[u] != -1:
                sack(heavy[u], True)

            for v in adj[u]:
                if v != heavy[u]:
                    for i in range(tin[v], tout[v] + 1):
                        add(tourValues[i])

            add(pathXor[u])

            for k, idx in nodeQueries[u]:
                if k > distinctCount:
                    ans[idx] = -1
                else:
                    ans[idx] = queryKth(k)

            if not keep:
                for i in range(tin[u], tout[u] + 1):
                    remove(tourValues[i])

        sack(0, True)
        return ans
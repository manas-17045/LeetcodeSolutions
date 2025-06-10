# Leetcode 2867: Count Valid Paths in a Tree
# https://leetcode.com/problems/count-valid-paths-in-a-tree/
# Solved on 10th of June, 2025

class Solution:
    def countPaths(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        isPrime = [True] * (n + 1)
        if n >= 0:
            isPrime[0] = False
        if n >= 1:
            isPrime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for multiple in range(i * i, (n + 1), i):
                    isPrime[multiple] = False

        dsuParent = list(range(n + 1))
        dsuSize = [1] * (n + 1)

        def findSet(i):
            root = i
            while dsuParent[root] != root:
                root = dsuParent[root]
            while dsuParent[i] != root:
                nextI = dsuParent[i]
                dsuParent[i] = root
                i = nextI
            return root

        def unionSets(i, j):
            rootI = findSet(i)
            rootJ = findSet(j)
            if rootI != rootJ:
                if dsuSize[rootI] < dsuSize[rootJ]:
                    rootI, rootJ = rootJ, rootI
                dsuParent[rootJ] = rootI
                dsuSize[rootI] += dsuSize[rootJ]

        for u, v in edges:
            if not isPrime[u] and not isPrime[v]:
                unionSets(u, v)

        totalPaths = 0

        for primeNode in range(1, n + 1):
            if isPrime[primeNode]:
                sumOfComponentSizes = 0
                pathsForPrime = 0

                neighborRoots = set()
                for neighbor in adj[primeNode]:
                    if not isPrime[neighbor]:
                        neighborRoots.add(findSet(neighbor))

                for root in neighborRoots:
                    compSize = dsuSize[root]
                    pathsForPrime += compSize * sumOfComponentSizes
                    sumOfComponentSizes += compSize

                pathsForPrime += sumOfComponentSizes
                totalPaths += pathsForPrime

        return totalPaths
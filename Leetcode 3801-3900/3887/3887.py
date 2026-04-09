# Leetcode 3887: Incremental Even-Weighted Cycle Queries
# https://leetcode.com/problems/incremetal-even-weighted-cycle-queries/
# Solved on 9th of April, 2026
class Solution:
    def numberOfEdgesAdded(self, n: int, edges: list[list[int]]) -> int:
        """
        Calculates the number of edges that can be added to maintain or create even-weighted cycles.

        :param n: The number of nodes in the graph.
        :param edges: A list of edges where each edge is represented as [u, v, w].
        :return: The total count of edges added based on parity constraints.
        """
        parentArray = list(range(n))
        distArray = [0] * n
        rankArray = [1] * n
        addedCount = 0

        def findRoot(node):
            if parentArray[node] == node:
                return node

            originalParent = parentArray[node]
            rootNode = findRoot(originalParent)
            distArray[node] = (distArray[node] + distArray[originalParent]) % 2
            parentArray[node] = rootNode
            return rootNode

        for u, v, w in edges:
            rootU = findRoot(u)
            rootV = findRoot(v)

            if rootU != rootV:
                if rankArray[rootU] > rankArray[rootV]:
                    parentArray[rootV] = rootU
                    distArray[rootV] = (w + distArray[u] - distArray[v]) % 2
                elif rankArray[rootU] < rankArray[rootV]:
                    parentArray[rootU] = rootV
                    distArray[rootU] = (w + distArray[v] - distArray[u]) % 2
                else:
                    parentArray[rootU] = rootV
                    distArray[rootU] = (w + distArray[v] - distArray[u]) % 2
                    rankArray[rootV] += 1
                addedCount += 1
            else:
                if (distArray[u] + distArray[v] + w) % 2 == 0:
                    addedCount += 1

        return addedCount
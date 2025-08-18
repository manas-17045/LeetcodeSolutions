# Leetcode 1627: Graph Connectivity With Threshold
# https://leetcode.com/problems/graph-connectivity-with-threshold/
# Solved on 18th of August, 2025
class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        """
        Determines if pairs of nodes are connected based on a given threshold.

        Two nodes i and j are connected if there exists a common divisor d > threshold
        such that d divides both i and j. This forms a graph where nodes are connected
        if they share a common factor greater than the threshold.

        :param n: The number of nodes, from 1 to n.
        :param threshold: The minimum common divisor required for two nodes to be connected.
        :param queries: A list of pairs [node1, node2] to check for connectivity.
        :return: A list of booleans, where each boolean indicates if the corresponding query pair is connected.
        """
        if threshold == 0:
            return [True] * len(queries)

        parentArr = list(range(n + 1))
        sizeArr = [1] * (n + 1)

        def find(nodeIndex: int) -> int:
            if parentArr[nodeIndex] == nodeIndex:
                return nodeIndex
            parentArr[nodeIndex] = find(parentArr[nodeIndex])
            return parentArr[nodeIndex]

        def union(nodeI: int, nodeJ: int):
            rootI = find(nodeI)
            rootJ = find(nodeJ)
            if rootI != rootJ:
                if sizeArr[rootI] < sizeArr[rootJ]:
                    rootI, rootJ = rootJ, rootI
                parentArr[rootJ] = rootI
                sizeArr[rootI] += sizeArr[rootJ]

        for divisor in range(threshold + 1, n + 1):
            for multiple in range(divisor * 2, n + 1, divisor):
                union(divisor, multiple)

        resultList = []
        for query in queries:
            firstNode = query[0]
            secondNode = query[1]
            resultList.append(find(firstNode) == find(secondNode))

        return resultList
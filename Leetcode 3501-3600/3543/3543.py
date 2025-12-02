# Leetcode 3543: Maximum Weighted K-Edge Path
# https://leetcode.com/problems/maximum-weighted-k-edge-path/
# Solved on 2nd of December, 2025
class Solution:
    def maxWeight(self, n: int, edges: list[list[int]], k: int, t: int) -> int:
        """
        Finds the maximum possible weight of a path with exactly k edges,
        where the total weight of the path does not exceed t.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing a directed edge from u to v with weight w.
            k (int): The exact number of edges required in the path.
            t (int): The maximum allowed total weight of the path.

        Returns:
            The maximum possible weight of such a path, or -1 if no such path exists.
        """
        nodeMasks = [1] * n
        limitMask = (1 << t) - 1

        for _ in range(k):
            nextNodeMasks = [0] * n
            pathFound = False
            for u, v, w in edges:
                if nodeMasks[u] > 0:
                    shiftedMask = (nodeMasks[u] << w) & limitMask
                    if shiftedMask > 0:
                        nextNodeMasks[v] |= shiftedMask
                        pathFound = True

            nodeMasks = nextNodeMasks
            if not pathFound:
                return -1

        totalMask = 0
        for mask in nodeMasks:
            totalMask |= mask

        if totalMask == 0:
            return -1

        return totalMask.bit_length() - 1
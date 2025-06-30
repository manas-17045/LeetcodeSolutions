# Leetcode 3530: Maximum Profit from Valid Topological Order in DAG
# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/
# Solved on 29th of June, 2025
class Solution:
    def maxProfit(self, n: int, edges: list[list[int]], score: list[int]) -> int:
        """
        Calculates the maximum profit from a valid topological order in a DAG.

        Args:
            n: The number of nodes in the DAG.
            edges: A list of lists representing the directed edges, where edges[i] = [u, v]
                   means there is a directed edge from node u to node v.
            score: A list of integers where score[i] is the score of node i.

        Returns:
            The maximum profit achievable.

        This problem is solved using dynamic programming with bitmasking.
        """
        predecessorMasks = [0] * n
        for u, v in edges:
            predecessorMasks[v] |= (1 << u)

        dpTable = [0] * (1 << n)

        for mask in range(1 << n):
            if mask > 0 and dpTable[mask] == 0:
                continue

            nodesPlacedCount = bin(mask).count('1')

            for i in range(n):
                if not (mask & (1 << i)):
                    if (predecessorMasks[i] & mask) == predecessorMasks[i]:
                        newMask = mask | (1 << i)
                        position = nodesPlacedCount + 1

                        newProfit = dpTable[mask] + score[i] * position

                        dpTable[newMask] = max(dpTable[newMask], newProfit)

        return dpTable[(1 << n) - 1]
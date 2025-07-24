# Leetcode 2322: Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
# Solved on 24th of July, 2025
import sys


class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        """
        Calculates the minimum possible score after removing two distinct edges from a tree.
        The score is defined as the maximum XOR sum among the three resulting connected components
        minus the minimum XOR sum among them.

        :param nums: A list of integers where nums[i] is the value of the i-th node.
        :param edges: A list of lists representing the edges of the tree.
        :return: The minimum score achievable.
        """

        n = len(nums)
        # The recursion limit might need to be increased for deep trees.
        sys.setrecursionlimit(n + 50)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        xorSum = [0] * n
        startTime = [0] * n
        endTime = [0] * n
        timer = 0

        def dfs(u: int, p: int) -> int:
            nonlocal timer
            startTime[u] = timer
            timer += 1

            currentXor = nums[0]
            for v in adj[u]:
                if v != p:
                    currentXor ^= dfs(v, u)

            xorSum[u] = currentXor
            endTime[u] = timer
            return currentXor

        dfs(0, -1)

        minScore = float('inf')
        totalXor = xorSum[0]

        for i in range(1, n):
            for j in range((i + 1), n):
                val1 = 0
                val2 = 0
                val3 = 0

                isIAncestorOfJ = (startTime[i] < startTime[j]) and (endTime[j] <= endTime[i])
                isJAncestorOfI = (startTime[j] < startTime[i]) and (endTime[i] <= endTime[j])

                if isIAncestorOfJ:
                    val1 = xorSum[j]
                    val2 = xorSum[i] ^ xorSum[j]
                    val3 = totalXor ^ xorSum[i]
                elif isJAncestorOfI:
                    val1 = xorSum[i]
                    val2 = xorSum[j] ^ xorSum[i]
                    val3 = totalXor ^ xorSum[j]
                else:
                    val1 = xorSum[i]
                    val2 = xorSum[j]
                    val3 = totalXor ^ xorSum[i] ^ xorSum[j]

                currentScore = max(val1, val2, val3) - min(val1, val2, val3)
                minScore = min(minScore, currentScore)

        return minScore
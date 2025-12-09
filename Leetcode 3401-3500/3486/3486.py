# Leetcode 3486: Longest Special Path II
# https://leetcode.com/problems/longest-special-path-ii/
# Solved on 9th of December, 2025
import sys
sys.setrecursionlimit(100000)


class Solution:
    def longestSpecialPath(self, edges: list[list[int]], nums: list[int]) -> list[int]:
        """
        Finds the longest "special" path in a tree. A path is special if it contains at least two nodes
        with the same value, and the subpath between the first two occurrences of that value
        (inclusive) contains at least three nodes. The length of the path is the sum of edge weights.

        Args:
            edges: A list of lists, where each inner list [u, v, w] represents an edge between nodes u and v with weight w.
            nums: A list of integers, where nums[i] is the value of node i.
        Returns:
            A list [maxLength, minNodes] representing the maximum length of a special path and the minimum number of nodes in such a path.
        """
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        maxVal = 0
        for x in nums:
            if x > maxVal:
                maxVal = x

        valueHistory = [[] for _ in range(maxVal + 1)]
        distMap = [0] * n

        # res = [maxLen, minNodes]
        res = [-1, 1]

        def dfs(u, p, depth, currentDist, left, dupStart):
            val = nums[u]
            distMap[depth] = currentDist

            history = valueHistory[val]
            history.append(depth)
            size = len(history)

            nextLeft = left
            nextDupStart = dupStart

            if size >= 3:
                firstIdx = history[size - 3]
                nextLeft = max(nextLeft, firstIdx + 1)
                if nextDupStart < nextLeft:
                    nextDupStart = -1

            if size >= 2:
                pairStart = history[size - 2]
                if pairStart >= nextLeft:
                    if nextDupStart != -1 and nextDupStart != pairStart:
                        nextLeft = max(nextLeft, min(nextDupStart, pairStart) + 1)
                        nextDupStart = max(nextDupStart, pairStart)
                    else:
                        nextDupStart = pairStart

            length = currentDist - distMap[nextLeft]
            nodes = depth - nextLeft + 1

            if length > res[0]:
                res[0] = length
                res[1] = nodes
            elif length == res[0]:
                res[1] = min(res[1], nodes)

            for v, w in adj[u]:
                if v != p:
                    dfs(v, u, depth + 1, currentDist + w, nextLeft, nextDupStart)

            history.pop()

        dfs(0, -1, 0, 0, 0, -1)
        return res

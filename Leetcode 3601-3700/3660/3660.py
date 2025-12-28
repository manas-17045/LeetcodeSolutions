# Leetcode 3660: Jump Game IX
# https://leetcode.com/problems/jump-game-ix/
# Solved on 28th of December, 2025
import sys
sys.setrecursionlimit(200000)


class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        """
        Calculates the maximum value reachable from each index in a given list of numbers,
        considering a specific jump game rule.

        :param nums: A list of integers representing the values at each position.
        :return: A list of integers where each element at index `i` is the maximum value reachable from `i`.
        """
        n = len(nums)
        parent = list(range(n))
        compMax = list(nums)

        def find(i):
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
            return i

        def union(i, j):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parent[rootI] = rootJ
                if compMax[rootI] > compMax[rootJ]:
                    compMax[rootJ] = compMax[rootI]

        stack = []

        for i in range(n):
            val = nums[i]
            if stack and stack[-1][0] > val:
                maxVal = stack[-1][0]
                rep = stack[-1][1]
                while stack and stack[-1][0] > val:
                    _, idx = stack.pop()
                    union(idx, i)
                stack.append((maxVal, rep))
            else:
                stack.append((val, i))

        result = []
        for i in range(n):
            result.append(compMax[find(i)])

        return result
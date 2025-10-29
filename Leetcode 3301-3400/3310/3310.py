# Leetcode 3310: Remove Methods From Project
# https://leetcode.com/problems/remove-methods-from-project/
# Solved on 29th of October, 2025
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        """
        Determines which methods can be removed from a project based on invocation dependencies.

        Args:
            n (int): The total number of methods, labeled from 0 to n-1.
            k (int): The index of the suspicious method.
            invocations (list[list[int]]): A list of [u, v] pairs indicating method u invokes method v.
        Returns:
            list[int]: A list of indices of methods that should remain in the project.
        """
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        isSuspicious = [False] * n
        stack = [k]
        isSuspicious[k] = True

        while stack:
            u= stack.pop()
            for v in adj[u]:
                if not isSuspicious[v]:
                    isSuspicious[v] = True
                    stack.append(v)

        canRemove = True
        for u in range(n):
            if not isSuspicious[u]:
                for v in adj[u]:
                    if isSuspicious[v]:
                        canRemove = False
                        break
            if not canRemove:
                break

        if not canRemove:
            return list(range(n))

        remaining = []
        for i in range(n):
            if not isSuspicious[i]:
                remaining.append(i)

        return remaining
# Leetcode 3327: Check if DFS Strings Are Palindromes
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/
# Solved on 26th of May, 2025
import sys


class Solution:
    def findAnswer(self, parent: list[int], s: str) -> list[bool]:
        """
        For each node in a tree, determine if the string formed by concatenating the characters
        of its subtree nodes in DFS order is a palindrome.

        Args:
            parent: A list representing the parent of each node. parent[i] is the parent of node i.
                    parent[0] is -1 as node 0 is the root.
            s: A string where s[i] is the character of node i.
        Returns:
            A list of booleans, where the i-th element is True if the subtree string of node i is a palindrome, False otherwise.
        """
        n = len(parent)
        # Build the tree in adjacency-list form
        tree: list[list[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        # These will record the [start, end] indices in dfsStr for each node's subtree
        start = [0] * n
        end = [0] * n
        dfsStr: list[str] = []

        # Increase recursion limit for deep trees
        sys.setrecursionlimit(10**7)

        def dfs(u: int, idx: int) -> int:
            start[u] = idx
            for v in tree[u]:
                idx = dfs(v, idx)
            end[u] = idx
            dfsStr.append(s[u])
            return idx + 1

        # Run DFS from the real root (0).
        dfs(0, 0)
        dfsStr = ''.join(dfsStr)    # Collapse into a single string of length n

        # Build the Manacher-friendly string with sentinels
        # Example: dfsStr = "aba" → T = ['^','#','a','#','b','#','a','#','$']
        T: list[str] = ['^']
        for ch in dfsStr:
            T.append('#')
            T.append(ch)
        T.extend(['#', '$'])

        m = len(T)
        p = [0] * m
        center = right = 0

        # Manacher's algorithm to fill p[i] = radius of palindrome around T[i].
        for i in range(1, m - 1):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])
            # Try to expand around i
            while T[i + p[i] + 1] == T[i - p[i] - 1]:
                p[i] += 1
            # Update the rightmost palindrome
            if i + p[i] > right:
                center, right = i, i + p[i]

        # For each node u, check if its subtree-DFS string (dfsStr[start[u]:end[u]+1])
        # is a palindrome. In T this substring maps to [2+2*l ... 2+2*r], so its center
        # is at c = 2 + (l + r), and its half-width in T is (r - l).
        ans = [False] * n
        for u in range(n):
            l, r = start[u], end[u]
            c = 2 + l + r
            if p[c] >= (r - l):
                ans[u] = True

        return ans
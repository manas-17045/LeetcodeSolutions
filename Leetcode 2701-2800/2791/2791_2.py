# Leetcode 2791: Count Paths That Can Form a Palindrome in a Tree
# https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/
# Solved on 11th of June, 2025
from collections import Counter


class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        """
        Counts the number of pairs of nodes (u, v) in a tree such that the path
        between u and v forms a palindrome.

        Args:
            parent: A list where parent[i] is the parent of node i. parent[0] is -1.
            s: A string where s[i] is the character at node i.

        Returns:
            The number of pairs of nodes (u, v) such that the path between u and v
            forms a palindrome.
        """
        n = len(parent)
        # Build children lists
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        # We'll do an iterative DFS from root = 0/
        stack = [(0, 0)]

        freq = Counter()
        freq[0] = 1

        ans = 0

        while stack:
            u, mask_u = stack.pop()

            # For each child, compute its mask
            for v in children[u]:
                # Flip the bit corresponding to s[v]
                bit = 1 << (ord(s[v]) - ord('a'))
                mask_v = mask_u ^ bit

                ans += freq[mask_v]

                for k in range(26):
                    ans += freq[mask_v ^ (1 << k)]

                # Now include v in freq and continue DFS
                freq[mask_v] += 1
                stack.append((v, mask_v))

        return ans
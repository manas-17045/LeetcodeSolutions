# Leetcode 2246: Longest Path With Different Adjacent Characters
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# Solved on 27th of June, 2025
import sys


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        """
        Calculates the length of the longest path in a tree such that no two adjacent nodes
        in the path have the same character.
        :param parent: A list where parent[i] is the parent of the i-th node. parent[0] is -1.
        :param s: A string where s[i] is the character assigned to the i-th node.
        :return: The length of the longest valid path.
        """
        sys.setrecursionlimit(10 ** 7)
        n = len(parent)

        # Build children adjacency list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        self.ans = 1    # At least one node

        def dfs(u: int) -> int:
            longest = second = 0

            for v in children[u]:
                length_v = dfs(v)

                # Can only attach v f its character differs
                if s[v] == s[u]:
                    continue

                # Keep top two lengths
                if length_v > longest:
                    second = longest
                    longest = length_v
                elif length_v > second:
                    second = length_v

            # Combine the two best child-paths through u
            self.ans = max(self.ans, longest + second + 1)

            # Return best single branch extended by u
            return 1 + longest

        dfs(0)
        return self.ans
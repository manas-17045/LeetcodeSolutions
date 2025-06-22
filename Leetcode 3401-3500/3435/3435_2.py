# Leetcode 3435: Frequencies of Shortest Supersequences
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/
# Solved on 21st of June, 2025
from itertools import combinations


class Solution:
    def supersequence(self, words: list[str]) -> list[list[int]]:
        """
        Given a list of two-letter words, finds the minimum-sized feedback vertex set (FVS)
        in the graph formed by these words. Each word "ab" represents a directed edge a -> b.
        The goal is to find a set of letters (nodes) to remove such that the remaining graph
        is acyclic. Among all such sets, we are interested in those with the minimum size.
        For each such minimum FVS, a frequency array of length 26 is constructed:
        - Letters not involved in any word (not in `unique_letters`) have a frequency of 0.
        - Letters involved in words but not in the FVS have a frequency of 1.
        - Letters in the FVS have a frequency of 2.

        Args:
            words: A list of two-letter strings, e.g., ["ab", "bc"].
        Returns:
            A list of 26-length integer lists, each representing a frequency array for a minimum FVS.
        """
        # Collect all distinct letters appearing in any word
        unique_letters = set()
        for w in words:
            unique_letters.add(ord(w[0]) - ord('a'))
            unique_letters.add(ord(w[1]) - ord('a'))
        # list of letter-indices
        nodes = sorted(unique_letters)
        n = len(nodes)
        letter2idx = {letter: i for i, letter in enumerate(nodes)}

        # Build adjacency list among the compact indices
        graph = [[] for _ in range(n)]
        for w in words:
            u = letter2idx[ord(w[0]) - ord('a')]
            v = letter2idx[ord(w[1]) - ord('a')]
            graph[u].append(v)

        # Cycle-check on the induced subgraph of "kept" nodes
        def isAcyclic(removed: set) -> bool:
            color = [0] * n

            def dfs(u):
                color[u] = 1
                for v in graph[u]:
                    # Skip any edge touching a removed node
                    if v in removed or u in removed:
                        continue
                    if color[v] == 1:
                        return True
                    if color[v] == 0 and not dfs(v):
                        return False
                color[u] = 2
                return True

            for u in range(n):
                if u not in removed and color[u] == 0:
                    if not dfs(u):
                        return False
            return True

        # Find all minimum-size removal sets that break all cycles
        min_fvs = []
        for k in range(n + 1):
            for combo in combinations(range(n), k):
                rem = set(combo)
                if isAcyclic(rem):
                    min_fvs.append(rem)
            if min_fvs:
                break

        # For each removal set, build the 26-length freq array
        ans = []
        for fvs in min_fvs:
            freq = [0] * 26
            # Each letter appears once
            for letter in nodes:
                freq[letter] = 1
            # Letters in the feedback set appear twice
            for idx in fvs:
                freq[nodes[idx]] = 2
            ans.append(freq)

        return ans
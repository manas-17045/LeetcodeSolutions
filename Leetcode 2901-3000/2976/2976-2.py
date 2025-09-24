# Leetcode 2976: Minimum Cost to Convert String I
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/
# Solved on 24th of September, 2025
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Calculates the minimum cost to transform the `source` string into the `target` string.
        The transformation involves changing characters based on a given set of `original` to `changed` character mappings, each with an associated `cost`.

        Args:
            source (str): The original string to be transformed.
            target (str): The desired target string.
            original (list[str]): A list of characters representing the original character in a transformation.
            changed (list[str]): A list of characters representing the character after transformation.
            cost (list[int]): A list of integers where cost[i] is the cost to change original[i] to changed[i].

        Returns:
            int: The minimum total cost to transform `source` to `target`. Returns -1 if transformation is impossible.
        """
        # If lengths differ, impossible (problem states equal but safe-guard)
        if len(source) != len(target):
            return -1

        INF = 10 ** 18
        K = 26
        # Distance matrix: min cost to convert i -> j
        dist = [[INF] * K for _ in range(K)]
        for i in range(K):
            dist[i][i] = 0

        # Initialize edges from given mappings (take min for duplicates)
        m = len(cost)
        for i in range(m):
            u = ord(original[i]) - 97
            v = ord(changed[i]) - 97
            if cost[i] < dist[u][v]:
                dist[u][v] = cost[i]

        # Floyd-Warshall over 26 nodes
        for k in range(K):
            dk = dist[k]
            for i in range(K):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                # Inner loop
                for j in range(K):
                    # Try path i->k->j
                    nk = dik + dk[j]
                    if nk < di[j]:
                        di[j] = nk

        total = 0
        n = len(source)
        for i in range(n):
            if source[i] == target[i]:
                continue
            u = ord(source[i]) - 97
            v = ord(target[i]) - 97
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]

        return total
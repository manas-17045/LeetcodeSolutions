# Leetcode 2977: Minimum Cost to Convert String II
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/
# Solved on 14th of September, 2025
import collections


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Calculates the minimum cost to transform the source string into the target string
        using a given set of character/substring transformations.

        Args:
            source (str): The original string to be transformed.
            target (str): The desired target string.
            original (list[str]): A list of original substrings that can be transformed.
            changed (list[str]): A list of substrings that original[i] can be changed into.
            cost (list[int]): The cost to change original[i] to changed[i].

        Returns:
            int: The minimum cost to transform source to target. Returns -1 if transformation is not possible.
        """
        INF = 10 ** 18
        n = len(source)
        # Build unique node list from all original/changed strings
        node_map = {}
        nodes = []

        def add_node(s: str) -> int:
            if s in node_map:
                return node_map[s]
            idx = len(nodes)
            nodes.append(s)
            node_map[s] = idx
            return idx

        for s in original:
            add_node(s)
        for s in changed:
            add_node(s)

        m = len(nodes)
        # length of each node string
        node_len = [len(s) for s in nodes]

        # distance matrix (only meaningful between nodes of same length)
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        # Add edges from original -> changed with given cost
        for o, cng, w in zip(original, changed, cost):
            u = node_map[o]
            v = node_map[cng]
            if w < dist[u][v]:
                dist[u][v] = w

        # Group nodes by length and run Floyd–Warshall inside each group
        groups = collections.defaultdict(list)
        for idx, L in enumerate(node_len):
            groups[L].append(idx)

        for L, idxs in groups.items():
            # Floyd-Warshall on idxs
            for k in idxs:
                dk = dist[k]
                for i in idxs:
                    if dist[i][k] == INF:
                        continue
                    dik = dist[i][k]
                    rowi = dist[i]
                    # try relax via k to all j in same-length group
                    for j in idxs:
                        val = dik + dk[j]
                        if val < rowi[j]:
                            rowi[j] = val

        # Precompute, for each start index in source, which rule indices' original pattern occurs there.
        matches = [[] for _ in range(n)]
        # Use Python str.find to locate occurrences efficiently
        for rid, pat in enumerate(original):
            start = 0
            while True:
                pos = source.find(pat, start)
                if pos == -1:
                    break
                matches[pos].append(rid)
                start = pos + 1

        # dp[pos] = min cost to convert prefix source[:pos] to target[:pos]
        dp = [INF] * (n + 1)
        dp[0] = 0

        for l in range(n):
            if dp[l] == INF:
                continue
            # If the single character matches, we can advance for free
            if source[l] == target[l]:
                if dp[l] < dp[l + 1]:
                    dp[l + 1] = dp[l]

            # Try every rule whose original starts at l
            for rid in matches[l]:
                L = len(original[rid])
                r = l + L
                if r > n:
                    continue
                tsub = target[l:r]
                # Only possible to transform whole substring to tsub if tsub is present in nodes
                if tsub in node_map:
                    u_idx = node_map[original[rid]]
                    v_idx = node_map[tsub]
                    c = dist[u_idx][v_idx]
                    if c < INF:
                        new_cost = dp[l] + c
                        if new_cost < dp[r]:
                            dp[r] = new_cost

        return -1 if dp[n] >= INF else dp[n]
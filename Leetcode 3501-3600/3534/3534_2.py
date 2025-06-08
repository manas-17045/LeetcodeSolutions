# Leetcode 3534: Path Existence Queries in a Graph II
# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
# Solved on 8th of June, 2025

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        """
        Given an array `nums` of length `n`, and a maximum difference `maxDiff`,
        we can move between two indices `i` and `j` if `abs(nums[i] - nums[j]) <= maxDiff`.
        We are given a list of queries `queries`, where each query `[u, v]` asks for
        the minimum number of moves required to go from index `u` to index `v`.

        The problem can be rephrased as finding the minimum number of hops in a graph
        where nodes are indices and an edge exists between `i` and `j` if
        `abs(nums[i] - nums[j]) <= maxDiff`.

        This solution uses sorting and binary lifting to efficiently answer queries.
        First, the array is sorted while keeping track of original indices. Then,
        a jump table is built using binary lifting to quickly find the farthest
        reachable index within `maxDiff`. Finally, queries are answered by finding
        the minimum hops using the precomputed jump table.
        """
        # Sort nums and remember each original index's position in the sorted array
        sorted_pairs = sorted((num, i) for i, num in enumerate(nums))
        sorted_vals = [p[0] for p in sorted_pairs]
        idx_map = [0] * n
        for sorted_i, (_, orig_i) in enumerate(sorted_pairs):
            idx_map[orig_i] = sorted_i

        # Build level-0 jump: for each i, the farthest j >= i such that
        # sorted_vals[j] - sorted_vals[i] <= maxDiff
        # We maintain a sliding window with`right` pointer
        LOG = (n - 1).bit_length() + 1
        jump = [[0] * LOG for _ in range(n)]
        right = 0
        for i in range(n):
            right = max(right, i)
            while right + 1 < n and sorted_vals[right + 1] - sorted_vals[i] <= maxDiff:
                right += 1
            jump[i][0] = right

        # Binary-lift to fill jump[i][k] - jump[jump[i][k-1]][k-1]
        for k in range(1, LOG):
            for i in range(n):
                jump[i][k] = jump[jump[i][k - 1]][k - 1]

        def minHops(s: int, t: int) -> int:
            """
            Return minimum number of hops to go from sorted-index s to reach >= t.
            """
            if s == t:
                return 0
            # One hop suffices?
            if jump[s][0] >= t:
                return 1
            # Even with all lifts, we can't reach
            if jump[s][LOG - 1] < t:
                return -1

            hops = 0
            cur = s
            # Greedily lift the largest bit that still lands us before t
            for k in reversed(range(LOG)):
                if jump[cur][k] < t:
                    hops += 1 << k
                    cur = jump[cur][k]
            # One more ho to go over the threshold
            return hops + 1

        # Answer each query
        ans = []
        for u, v in queries:
            iu, iv = idx_map[u], idx_map[v]
            lo, hi = min(iu, iv), max(iu, iv)
            ans.append(minHops(lo, hi))
        return ans
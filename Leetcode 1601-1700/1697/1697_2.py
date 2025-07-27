# Leetcode 1697: Checking Existence of Edge Length Limited Paths
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
# Solved on 27th of July, 2025
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """
        Determines for each query if there is a path between two nodes such that all edge weights along the path
        are strictly less than a given limit.
        :param n: The number of nodes in the graph.
        :param edgeList: A list of edges, where each edge is [u, v, weight].
        :param queries: A list of queries, where each query is [p, q, limit].
        :return: A list of booleans, where ans[i] is true if a path exists for queries[i] and false otherwise.
        """
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # Union by rank
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        # Sort edges by weight (distance)
        edgeList.sort(key=lambda e: e[2])

        # Augment queries with original indices and sort by limit
        # Each query: (p, q, limit, original_index)
        qs = [(p, q, lim, i) for i, (p, q, lim) in enumerate(queries)]
        qs.sort(key=lambda x: x[2])

        ans = [False] * len(queries)
        ei = 0  # pointer into edgeList

        # Process queries in order of increasing limit
        for p, q, lim, qi in qs:
            # Add all edges with weight < lim
            while ei < len(edgeList) and edgeList[ei][2] < lim:
                u, v, _w = edgeList[ei]
                union(u, v)
                ei += 1

            # After adding, check connectivity
            ans[qi] = (find(p) == find(q))

        return ans
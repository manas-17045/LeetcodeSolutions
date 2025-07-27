# Leetcode 1697: Checking Existence of Edge Length Limited Paths
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
# Solved on 27th of July, 2025
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """
        Checks if paths exist between pairs of nodes with all edge weights less than a given limit.

        Args:
            n (int): The number of nodes in the graph.
            edgeList (list[list[int]]): A list of edges, where each edge is [u, v, weight].
            queries (list[list[int]]): A list of queries, where each query is [p, q, limit].
        Returns:
            list[bool]: A list of booleans, where each boolean indicates if a path exists for the corresponding query.
        """
        parent = list(range(n))

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(nodeA, nodeB):
            rootA = find(nodeA)
            rootB = find(nodeB)
            if rootA != rootB:
                parent[rootB] = rootA

        edgeList.sort(key=lambda x: x[2])

        queriesWithIndex = []
        for i, query in enumerate(queries):
            queriesWithIndex.append(query + [i])

        queriesWithIndex.sort(key=lambda x: x[2])

        answer = [False] * len(queries)
        edgePointer = 0

        for p, q, limit, queryIndex in queriesWithIndex:
            while edgePointer < len(edgeList) and edgeList[edgePointer][2] < limit:
                u, v, _ = edgeList[edgePointer]
                union(u, v)
                edgePointer += 1

            if find(p) == find(q):
                answer[queryIndex] = True

        return answer
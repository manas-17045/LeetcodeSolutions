# Leetcode 3311: Construct 2D Grid Matching Graph Layout
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/
# Solved on 20th of June, 2025
class Solution:
    def constructGridLayout(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        Constructs a grid layout of nodes given the number of nodes and the edges
        connecting them. The graph is assumed to be a grid graph.

        The algorithm works by first identifying a corner node (a node with the minimum degree).
        It then constructs the first row by traversing neighbors of the corner node,
        prioritizing neighbors with degrees equal to the corner's degree or corner's degree + 1.
        Subsequent rows are filled by finding unseen neighbors of the nodes in the row above.

        Args:
            n: The total number of nodes.
            edges: A list of edges, where each edge is a list [u, v] representing a connection between nodes u and v.
        Returns:
            A list of lists representing the grid layout of the nodes.
        """
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Record degrees
        deg = [len(nei) for nei in graph]

        # Choose corner = node of minimal degree
        corner = min(range(n), key=lambda i: deg[i])

        # Sort each adjacency list by neighbor-degree ascending
        for u in range(n):
            graph[u].sort(key=lambda v: deg[v])

        seen = [False] * n
        seen[corner] = True

        # Build the first row starting from corner
        firstRow = [corner]
        cornerDeg = deg[corner]

        while len(firstRow) == 1 or deg[firstRow[-1]] == cornerDeg + 1:
            last = firstRow[-1]
            for v in graph[last]:
                # Allowed degrees are corner_deg (if it's second corner) or corner_deg + 1
                if not seen[v] and (deg[v] == cornerDeg or deg[v] == (cornerDeg + 1)):
                    seen[v] = True
                    firstRow.append(v)
                    break

            else:
                # If no neighbor fits, stop
                break

        cols = len(firstRow)
        rows = n // cols

        # Allocate answer matrix
        ans = [[-1] * cols for _ in range(rows)]
        ans[0] = firstRow

        # Fill subsequent rows column by column
        for i in range(1, rows):
            for j in range(cols):
                prev = ans[i - 1][j]
                # Pick any unseen neighbor of prev
                for v in graph[prev]:
                    if not seen[v]:
                        seen[v] = True
                        ans[i][j] = v
                        break


        return ans
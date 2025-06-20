# Leetcode 3311: Construct 2D Grid Matching Graph Layout
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/
# Solved on 20th of June, 2025
import collections


class Solution:
    def constructGridlayout(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        Constructs a 2D grid layout of nodes based on a given graph structure.

        The graph is assumed to represent a grid where nodes are connected to their
        adjacent neighbors (up, down, left, right). The algorithm identifies a
        corner node (a node with the minimum degree) and uses it as the starting
        point to build the first row of the grid. Subsequent rows are constructed
        by finding unvisited neighbors of the nodes in the row above.

        Args:
            n: The total number of nodes in the graph.
            edges: A list of lists representing the edges of the graph, where each
                   inner list [u, v] indicates an edge between nodes u and v.

        Returns:
            A 2D list representing the grid layout of the nodes. The dimensions of
            the grid are determined by the length of the first row found.
        """
        graph = collections.defaultdict(list)
        degrees = [0] * n

        for u, vNode in edges:
            graph[u].append(vNode)
            graph[vNode].append(u)
            degrees[u] += 1
            degrees[vNode] += 1

        minDegreeVal = float('inf')
        cornerNode = -1
        for i in range(n):
            if degrees[i] < minDegreeVal:
                minDegreeVal = degrees[i]
                cornerNode = i

        seen = [False] * n
        seen[cornerNode] = True

        cornerNodeDegree = degrees[cornerNode]
        firstRow = [cornerNode]

        while len(firstRow) == 1 or degrees[firstRow[-1]] == cornerNodeDegree + 1:
            currentNode = firstRow[-1]

            neighborsToConsider = sorted(graph[currentNode], key=lambda neighborNode: degrees[neighborNode])

            foundNextInRow = False
            for vNeighbor in neighborsToConsider:
                if not seen[vNeighbor] and (degrees[vNeighbor] == cornerNodeDegree or degrees[vNeighbor] == (cornerNodeDegree + 1)):
                    firstRow.append(vNeighbor)
                    seen[vNeighbor] = True
                    foundNextInRow = True
                    break

            if not foundNextInRow:
                break

        numCols = len(firstRow)
        numRows = n // numCols

        ansGrid = [[0] * numCols for _ in range(numRows)]

        ansGrid[0] = firstRow[:]

        for rIdx in range(1, numRows):
            for cIdx in range(numCols):
                nodeAbove = ansGrid[rIdx - 1][cIdx]
                for neighborOfNodeAbove in graph[nodeAbove]:
                    if not seen[neighborOfNodeAbove]:
                        ansGrid[rIdx][cIdx] = neighborOfNodeAbove
                        seen[neighborOfNodeAbove] = True
                        break

        return ansGrid
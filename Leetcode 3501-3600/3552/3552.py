# Leetcode 3552: Grid Teleportation Traversal
# https://leetcode.com/problems/grid-teleportation-traversal/
# Solved on 30th of December, 2025
import collections


class Solution:
    def minMoves(self, matrix: list[str]) -> int:
        """
        Calculates the minimum number of moves required to travel from the top-left corner (0,0)
        to the bottom-right corner (rows-1, cols-1) of a grid.

        :param matrix: A list of strings representing the grid. Each character can be '.', '#', or an uppercase letter.
        :return: The minimum number of moves as an integer, or -1 if the destination is unreachable.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        portalLocations = collections.defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                char = matrix[r][c]
                if 'A' <= char <= 'Z':
                    portalLocations[char].append((r, c))

        distances = [[float('inf')] * cols for _ in range(rows)]
        distances[0][0] = 0
        deque = collections.deque([(0, 0)])
        visitedPortals = set()

        while deque:
            row, col = deque.popleft()
            currentDist = distances[row][col]

            if row == rows - 1 and col == cols - 1:
                return int(currentDist)

            cellValue = matrix[row][col]
            if 'A' <= cellValue <= 'Z' and cellValue not in visitedPortals:
                visitedPortals.add(cellValue)
                for portalRow, portalCol in portalLocations[cellValue]:
                    if currentDist < distances[portalRow][portalCol]:
                        distances[portalRow][portalCol] = currentDist
                        deque.appendleft((portalRow, portalCol))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dRow, dCol in directions:
                newRow, newCol = row + dRow, col + dCol
                if 0 <= newRow < rows and 0 <= newCol < cols:
                    if matrix[newRow][newCol] != '#':
                        if currentDist + 1 < distances[newRow][newCol]:
                            distances[newRow][newCol] = currentDist + 1
                            deque.append((newRow, newCol))

        return -1
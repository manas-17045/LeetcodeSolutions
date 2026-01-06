# Leetcode 2850: Minimum Moves to Spread Stones Over Grid
# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/
# Solved on 6th of January, 2026
from itertools import permutations


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of moves required to spread stones evenly over a 3x3 grid.
        An even spread means each cell has exactly one stone.

        :param grid: A 3x3 list of lists representing the grid, where each cell contains the number of stones.
        :return: The minimum total Manhattan distance required to move stones to achieve an even spread.
        """
        emptyCells = []
        extraStones = []

        for row in range(3):
            for col in range(3):
                cellValue = grid[row][col]
                if cellValue == 0:
                    emptyCells.append((row, col))
                elif cellValue > 1:
                    extraCount = cellValue - 1
                    for _ in range(extraCount):
                        extraStones.append((row, col))

        minTotalMoves = float('inf')

        for currentPermutation in permutations(emptyCells):
            currentMoves = 0
            for source, target in zip(extraStones, currentPermutation):
                currentMoves += abs(source[0] - target[0]) + abs(source[1] - target[1])

            if currentMoves < minTotalMoves:
                minTotalMoves = currentMoves

        return minTotalMoves
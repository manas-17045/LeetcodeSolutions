# Leetcode 1284: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
# Solved on 25th of July, 2025
import collections


class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        """
        Calculates the minimum number of flips required to convert a binary matrix to a zero matrix.

        Args:
            mat (list[list[int]]): The input binary matrix.
        Returns:
            int: The minimum number of flips, or -1 if it's impossible.
        """

        numRows = len(mat)
        numCols = len(mat[0])

        initialState = 0
        for row in range(numRows):
            for col in range(numCols):
                if mat[row][col] == 1:
                    initialState |= (1 << (row * numCols + col))

        if initialState == 0:
            return 0

        bfsQueue = collections.deque([(initialState, 0)])
        visitedStates = {initialState}

        while bfsQueue:
            currentState, flips = bfsQueue.popleft()

            for row in range(numRows):
                for col in range(numCols):
                    nextState = currentState

                    indicesToFlip = [(row, col)]
                    if row > 0:
                        indicesToFlip.append((row - 1, col))
                    if row < numRows - 1:
                        indicesToFlip.append((row + 1, col))
                    if col > 0:
                        indicesToFlip.append((row, col - 1))
                    if col < numCols - 1:
                        indicesToFlip.append((row, col + 1))

                    for r, c in indicesToFlip:
                        nextState ^= (1 << (r * numCols + c))

                    if nextState == 0:
                        return flips + 1

                    if nextState not in visitedStates:
                        visitedStates.add(nextState)
                        bfsQueue.append((nextState, flips + 1))

        return -1
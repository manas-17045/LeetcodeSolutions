# Leetcode 3256: Maximum Value Sum by Placing Three Rooks I
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/
# Solved on 13th of December, 2025
class Solution:
    def maximumValueSum(self, board: list[list[int]]) -> int:
        """
        Calculates the maximum value sum by placing three rooks on a chessboard such that no two rooks share the same row or column.

        Args:
            board: A list of lists of integers representing the chessboard, where board[i][j] is the value at cell (i, j).
        Returns:
            The maximum possible sum of values of the three rooks.
        """
        numRows = len(board)
        numCols = len(board[0])
        bestInRow = []

        for r in range(numRows):
            currentRow = []
            for c in range(numCols):
                currentRow.append((board[r][c], c))
            currentRow.sort(key=lambda x: x[0], reverse=True)
            bestInRow.append(currentRow[:3])

        maxSum = -float('inf')

        for r1 in range(numRows):
            for r2 in range(r1 + 1, numRows):
                for r3 in range(r2 + 1, numRows):
                    for val1, col1 in bestInRow[r1]:
                        for val2, col2 in bestInRow[r2]:
                            if col1 == col2:
                                continue
                            for val3, col3 in bestInRow[r3]:
                                if col3 == col1 or col3 == col2:
                                    continue

                                currentSum = val1 + val2 + val3
                                if currentSum > maxSum:
                                    maxSum = currentSum

        return maxSum
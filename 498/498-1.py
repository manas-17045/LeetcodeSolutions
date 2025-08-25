# Leetcode 498: Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/
# Solved on 25th of August, 2025
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        Finds the diagonal order traversal of a given matrix.

        Args:
            mat: The input matrix (list of lists of integers).
        Returns:
            A list of integers representing the diagonal order traversal of the matrix.
        """
        if not mat or not mat[0]:
            return []

        numRows = len(mat)
        numCols = len(mat[0])
        result = [0] * (numRows * numCols)
        row = 0
        col = 0

        for i in range(numRows * numCols):
            result[i] = mat[row][col]

            # Even sum -> moving up
            if (row + col) % 2 == 0:
                if col == numCols - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            # Odd sum -> moving down
            else:
                if row == numRows - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return result
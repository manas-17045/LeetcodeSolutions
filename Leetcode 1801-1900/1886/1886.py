# Leetcode 1886: Determine Whether Matrix Can Be Obtained By Rotation
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtaibed-by-rotation/
# Solved on 22nd of March, 2026
class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        """
        Determines if the input matrix can be rotated in 90-degree increments to match the target matrix.

        Args:
            mat (list[list[int]]): The initial n x n square matrix.
            target (list[list[int]]): The target n x n square matrix to compare against.

        Returns:
            bool: True if mat can be rotated to match target, False otherwise.
        """
        matrixSize = len(mat)
        for rotationCount in range(4):
            if mat == target:
                return True

            for rowIdx in range(matrixSize // 2):
                for colIdx in range((matrixSize + 1) // 2):
                    tempVal = mat[rowIdx][colIdx]
                    mat[rowIdx][colIdx] = mat[matrixSize - 1 - colIdx][rowIdx]
                    mat[matrixSize - 1 - colIdx][rowIdx] = mat[matrixSize - 1 - rowIdx][matrixSize - 1 - colIdx]
                    mat[matrixSize - 1 - rowIdx][matrixSize - 1 - colIdx] = mat[colIdx][matrixSize - 1 - rowIdx]
                    mat[colIdx][matrixSize - 1 - rowIdx] = tempVal

        return False
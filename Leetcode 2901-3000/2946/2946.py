# Leetcode 2946: Matrix Similarity After Cyclic Shifts
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
# Solved on 27th of March, 2026
class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        """
        Determines if the matrix remains the same after cyclic shifts.

        :param mat: A 2D list of integers representing the matrix.
        :param k: An integer representing the number of cyclic shifts.
        :return: True if the matrix is similar to the original after shifts, False otherwise.
        """
        numRows = len(mat)
        numCols = len(mat[0])

        for i in range(numRows):
            for j in range(numCols):
                if mat[i][j] != mat[i][(j + k) % numCols]:
                    return False

        return True
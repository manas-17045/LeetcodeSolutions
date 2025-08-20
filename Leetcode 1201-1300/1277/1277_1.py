# Leetcode 1277: Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Solved on 20th of August, 2025
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        Counts the number of square submatrices with all ones in the given matrix.

        Args:
            matrix: A list of lists of integers representing the binary matrix.

        Returns:
            An integer representing the total count of square submatrices with all ones.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                count += matrix[i][j]

        return count
# Leetcode 1277: Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Solved on 20th of August, 2025
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        Counts the number of square submatrices with all ones.
        :param matrix: A list of lists of integers representing the binary matrix.
        :return: The total number of square submatrices with all ones.
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # If not on top row or left column, we can extend squares
                    if i > 0 and j > 0:
                        matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                    total += matrix[i][j]

        return total
# Leetcode 2133: Check if Every Row and Column Contains All Numbers
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
# Solved on 30th of August, 2025
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        """
        Checks if every row and every column in the given matrix contains all numbers from 1 to n (inclusive),
        where n is the dimension of the square matrix.

        Args:
            matrix (list[list[int]]): The input square matrix.
        Returns:
            bool: True if every row and column contains all numbers from 1 to n, False otherwise.
        """
        n = len(matrix)

        for i in range(n):
            rowSet = set()
            colSet = set()

            for j in range(n):
                rowSet.add(matrix[i][j])
                colSet.add(matrix[j][i])

            if len(rowSet) != n or len(colSet) != n:
                return False

        return True
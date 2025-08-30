# Leetcode 2133: Check if Every Row and Column Contains All Numbers
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
# Solved on 30th of August, 2025
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        """
        Checks if the given n x n integer matrix is valid.
        A matrix is valid if every row and every column contains all the integers from 1 to n (inclusive) exactly once.

        Args:
            matrix (list[list[int]]): The input n x n integer matrix.
        Returns:
            bool: True if the matrix is valid, False otherwise.
        """
        n = len(matrix)
        if n == 0:
            return True
        target = (1 << n) - 1  # bitmask with n ones: all values 1...n present -> matches this

        # Check rows
        for i in range(n):
            seen = 0
            for val in matrix[i]:
                if val < 1 or val > n:
                    return False
                bit = 1 << (val - 1)
                if seen & bit:
                    return False  # duplicate in the row
                seen |= bit
            if seen != target:
                return False  # some number missing in the row

        # Check columns
        for j in range(n):
            seen = 0
            for i in range(n):
                val = matrix[i][j]
                if val < 1 or val > n:
                    return False
                bit = 1 << (val - 1)
                if seen & bit:
                    return False  # duplicate in the column
                seen |= bit
            if seen != target:
                return False  # some number missing in the column

        return True
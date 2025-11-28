# Leetcode 1738: Find Kth Largest XOR Coordinate Value
# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
# Solved on 28th of November, 2025
class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        """
        Finds the Kth largest XOR coordinate value in a given matrix.

        The XOR coordinate value at (r, c) is the XOR sum of all elements in the submatrix
        from (0, 0) to (r, c).

        Args:
            matrix (list[list[int]]): The input matrix of integers.
            k (int): The rank of the largest XOR coordinate value to find.
        Returns:
            int: The Kth largest XOR coordinate value.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        xorCoordinates = []

        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    matrix[r][c] ^= matrix[r - 1][c]
                if c > 0:
                    matrix[r][c] ^= matrix[r][c - 1]
                if r > 0 and c > 0:
                    matrix[r][c] ^= matrix[r - 1][c - 1]
                xorCoordinates.append(matrix[r][c])

        xorCoordinates.sort(reverse=True)
        return xorCoordinates[k - 1]
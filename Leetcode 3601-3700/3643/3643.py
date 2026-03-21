# Leetcode 3643: Flip Square Submatrix Vertically
# https://leetcode.com/problems/flip-square-submatrix-vertically/
# Solved on 21st of March, 2026
class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        """
        Flips a square submatrix of size k by k vertically within a given grid.

        :param grid: The 2D list of integers representing the matrix.
        :param x: The starting row index of the submatrix.
        :param y: The starting column index of the submatrix.
        :param k: The size of the square submatrix to flip.
        :return: The modified grid with the submatrix flipped vertically.
        """
        for i in range(k // 2):
            topRow = x + i
            bottomRow = x + k - 1 - i

            grid[topRow][y:y + k], grid[bottomRow][y:y + k] = grid[bottomRow][y:y + k], grid[topRow][y:y + k]

        return grid
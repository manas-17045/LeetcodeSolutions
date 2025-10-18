# Leetcode 2906: Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/
# Solved on 18th of October, 2025
class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Constructs a product matrix where each element productMatrix[i][j] is the product of all elements in the input grid
        except for grid[i][j] itself, modulo 12345.

        Args:
            grid: A 2D list of integers representing the input grid.
        Returns:
            A 2D list of integers representing the product matrix.
        """
        n = len(grid)
        m = len(grid[0])
        modNum = 12345

        productMatrix = [[1] * m for _ in range(n)]

        prefixProduct = 1
        for i in range(n):
            for j in range(m):
                productMatrix[i][j] = prefixProduct
                prefixProduct = (prefixProduct * (grid[i][j] % modNum)) % modNum

        suffixProduct = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                productMatrix[i][j] = (productMatrix[i][j] * suffixProduct) % modNum
                suffixProduct = (suffixProduct * (grid[i][j] % modNum)) % modNum

        return productMatrix
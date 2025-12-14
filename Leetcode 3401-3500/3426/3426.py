# Leetcode 3426: Manhattan Distances of All Arrangements of Pieces
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/
# Solved on 14th of December, 2025
class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        """
        Calculates the sum of Manhattan distances of all arrangements of k pieces on an m x n grid.

        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.
            k: The number of pieces to place on the grid.

        Returns:
            The sum of Manhattan distances.
        """

        mod = 1000000007
        totalCells = m * n
        targetK = k - 2
        targetRest = totalCells - k
        limit = totalCells - 2

        currentFact = 1
        denomK = 1
        denomRest = 1

        for i in range(1, limit + 1):
            currentFact = (currentFact * i) % mod
            if i == targetK:
                denomK = currentFact
            if i == targetRest:
                denomRest = currentFact

        numerator = currentFact
        denomTotal = (denomK * denomRest) % mod
        combinations = (numerator * pow(denomTotal, mod - 2, mod)) % mod

        geometricTerm = (totalCells * (totalCells - 1)) % mod
        geometricTerm = (geometricTerm * (m + n)) % mod

        inv6 = pow(6, mod - 2, mod)

        result = (combinations * geometricTerm) % mod
        result = (result * inv6) % mod

        return result
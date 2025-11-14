# Leetcode 2536: Increment Submatrices by One
# https://leetcode.com/problems/increment-submatrices-by-one/
# Solved on 14th of November, 2025
class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        """
        Applies a series of range increment queries to an n x n matrix.
        Each query specifies a submatrix to increment by one.

        Args:
            n (int): The dimension of the square matrix.
            queries (list[list[int]]): A list of queries, where each query is [r1, c1, r2, c2]
                                       representing the top-left (r1, c1) and bottom-right (r2, c2)
                                       coordinates of the submatrix to increment.

        Returns:
            list[list[int]]: The final n x n matrix after all queries have been applied.
        """
        diffMat = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diffMat[r1][c1] += 1
            diffMat[r1][c2 + 1] -= 1
            diffMat[r2 + 1][c1] -= 1
            diffMat[r2 + 1][c2 + 1] += 1

        resultMat = [[0] * n for _ in range(n)]

        for r in range(n):
            rowSum = 0
            for c in range(n):
                rowSum += diffMat[r][c]
                if r > 0:
                    resultMat[r][c] = rowSum + resultMat[r - 1][c]
                else:
                    resultMat[r][c] = rowSum

        return resultMat
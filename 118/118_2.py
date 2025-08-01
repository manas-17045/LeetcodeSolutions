# Leetcode 118: Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Solved on 1st of August, 2025
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        Generates the first `numRows` rows of Pascal's Triangle.
        :param numRows: The number of rows to generate.
        :return: A list of lists of integers representing Pascal's Triangle.
        """
        if numRows <= 0:
            return []
        
        res: list[list[int]] = [[1]]

        for i in range(1, numRows):
            prev = res[-1]
            # Start and end with 1s
            row = [1] * (i + 1)

            # Each interior element is sum of two above
            for j in range(1, i):
                row[j] = prev[j - 1] + prev[j]

            res.append(row)

        return res
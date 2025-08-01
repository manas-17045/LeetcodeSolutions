# Leetcode 118: Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Solved on 1st of August, 2025
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        Generates the first `numRows` of Pascal's triangle.

        Args:
            numRows (int): The number of rows to generate.
        Returns:
            list[list[int]]: A list of lists representing Pascal's triangle.
        """
        if numRows == 0:
            return []
        
        pascalTriangle = [[1]]

        for i in range(1, numRows):
            previousRow = pascalTriangle[-1]
            currentRow = [1]

            for j in range(len(previousRow) - 1):
                sumOfElements = previousRow[j] + previousRow[j + 1]
                currentRow.append(sumOfElements)

            currentRow.append(1)
            pascalTriangle.append(currentRow)

        return pascalTriangle
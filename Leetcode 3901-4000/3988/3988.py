# Leetcode 3988: Create Grid With Exactly K Paths I
# https://leetcode.com/problems/create-grid-with-exactly-paths-i/
# Solved on 9th of August, 2026
class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        """
        Creates a grid with exactly k paths from (0, 0) to (m-1, n-1).
        
        Args:
            m: The number of rows.
            n: The number of columns.
            k: The number of paths.
        
        Returns:
            The grid with exactly k paths.
        """
        if k == 1:
            gridResult = [["#" for colIndex in range(n)] for rowIndex in range(m)]
            for rowIndex in range(m):
                gridResult[rowIndex][0] = "."
            for colIndex in range(n):
                gridResult[m - 1][colIndex] = "."
            return ["".join(rowCells) for rowCells in gridResult]

        if k == 2:
            if m < 2 or n < 2:
                return []
            gridResult = [["#" for colIndex in range(n)] for rowIndex in range(m)]
            for rowIndex in range(2):
                for colIndex in range(2):
                    gridResult[rowIndex][colIndex] = "."
            for rowIndex in range(1, m):
                gridResult[rowIndex][1] = "."
            for colIndex in range(1, n):
                gridResult[m - 1][colIndex] = "."
            return ["".join(rowCells) for rowCells in gridResult]

        if k == 3:
            if m >= 2 and n >= 3:
                gridResult = [["#" for colIndex in range(n)] for rowIndex in range(m)]
                for rowIndex in range(2):
                    for colIndex in range(3):
                        gridResult[rowIndex][colIndex] = "."
                for rowIndex in range(1, m):
                    gridResult[rowIndex][2] = "."
                for colIndex in range(2, n):
                    gridResult[m - 1][colIndex] = "."
                return ["".join(rowCells) for rowCells in gridResult]
            elif m >= 3 and n >= 2:
                gridResult = [["#" for colIndex in range(n)] for rowIndex in range(m)]
                for rowIndex in range(3):
                    for colIndex in range(2):
                        gridResult[rowIndex][colIndex] = "."
                for rowIndex in range(2, m):
                    gridResult[rowIndex][1] = "."
                for colIndex in range(1, n):
                    gridResult[m - 1][colIndex] = "."
                return ["".join(rowCells) for rowCells in gridResult]
            else:
                return []

        if k == 4:
            if m >= 3 and n >= 3:
                gridResult = [["#" for colIndex in range(n)] for rowIndex in range(m)]
                for rowIndex in range(3):
                    for colIndex in range(3):
                        gridResult[rowIndex][colIndex] = "."
                gridResult[0][2] = "#"
                gridResult[2][0] = "#"
                for rowIndex in range(2, m):
                    gridResult[rowIndex][2] = "."
                for colIndex in range(2, n):
                    gridResult[m - 1][colIndex] = "."
                return ["".join(rowCells) for rowCells in gridResult]
            elif m >= 2 and n >= 4:
                gridResult = [["#" for colIndex in range(n)] for rowIndex in range(m)]
                for rowIndex in range(2):
                    for colIndex in range(4):
                        gridResult[rowIndex][colIndex] = "."
                for rowIndex in range(1, m):
                    gridResult[rowIndex][3] = "."
                for colIndex in range(3, n):
                    gridResult[m - 1][colIndex] = "."
                return ["".join(rowCells) for rowCells in gridResult]
            elif m >= 4 and n >= 2:
                gridResult = [["#" for colIndex in range(n)] for rowIndex in range(m)]
                for rowIndex in range(4):
                    for colIndex in range(2):
                        gridResult[rowIndex][colIndex] = "."
                for rowIndex in range(3, m):
                    gridResult[rowIndex][1] = "."
                for colIndex in range(1, n):
                    gridResult[m - 1][colIndex] = "."
                return ["".join(rowCells) for rowCells in gridResult]
            else:
                return []

        return []
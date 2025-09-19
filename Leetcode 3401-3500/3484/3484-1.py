# Leetcode 3484: Design Spreadsheet
# https://leetcode.com/problems/design-spreadsheet/
# Solved on 19th of September, 2025
class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * rows for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        rowIndex, colIndex = self._parseCell(cell)
        self.grid[rowIndex][colIndex] = value

    def resetCell(self, cell: str) -> None:
        rowIndex, colIndex = self._parseCell(cell)
        self.grid[rowIndex][colIndex] = 0

    def getValue(self, formula: str) -> int:
        formulaParts = formula[1:].split('+')
        firstTerm = self._getTermValue(formulaParts[0])
        secondTerm = self._getTermValue(formulaParts[1])
        return firstTerm + secondTerm

    def _parseCell(self, cell: str) -> tuple[int, int]:
        colIndex = ord(cell[0]) - ord('A')
        rowIndex = int(cell[1:]) - 1
        return rowIndex, colIndex

    def _getTermValue(self, term: str) -> int:
        if 'A' <= term[0] <= 'Z':
            rowIndex, colIndex = self._parseCell(term)
            return self.grid[rowIndex][colIndex]
        else:
            return int(term)
# Leetcode 3484: Design Spreadsheet
# https://leetcode.com/problems/design-spreadsheet/
# Solved on 19th of September, 2025
class Spreadsheet:

    def __init__(self, rows: int):
        # Only store cells that have been explicitly set: key -> (col_idx, row_idx)
        self.rows = rows
        self._cells: dict[tuple[int,int], int] = {}

    def _parse_cell(self, cell: str) -> tuple[int,int]:
        # Cell format: Letter (A-Z) + row number (1-indexed)
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        return (col, row)

    def setCell(self, cell: str, value: int) -> None:
        key = self._parse_cell(cell)
        self._cells[key] = value

    def resetCell(self, cell: str) -> None:
        key = self._parse_cell(cell)
        if key in self._cells:
            del self._cells[key]

    def getValue(self, formula: str) -> int:
        # Formula format: "=X+Y" where X and Y are either cell refs or non-negative integers
        assert formula and formula[0] == '='
        expr = formula[1:]
        left, right = expr.split('+', 1)

        def operand_value(tok: str) -> int:
            tok = tok.strip()
            if tok.isdigit():
                return int(tok)
            # Otherwise treat as cell reference
            key = self._parse_cell(tok)
            return self._cells.get(key, 0)

        return operand_value(left) + operand_value(right)
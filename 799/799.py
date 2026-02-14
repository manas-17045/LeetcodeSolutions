# Leetcode 799: Champagne Tower
# https://leetcode.com/problems/champagne-tower/
# Solved on 14th of February, 2026
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Calculates how full a specific glass is in a champagne tower after pouring a certain amount.

        :param poured: The total number of cups of champagne poured into the top glass.
        :param query_row: The 0-indexed row of the glass to check.
        :param query_glass: The 0-indexed index of the glass in the row to check.
        :return: The amount of champagne in the specified glass, capped at 1.0.
        """
        currentRow = [float(poured)]
        for rowIndex in range(query_row):
            nextRow = [0.0] * (len(currentRow) + 1)
            for glassIndex in range(len(currentRow)):
                excessAmount = (currentRow[glassIndex] - 1.0) / 2.0

                if excessAmount > 0:
                    nextRow[glassIndex] += excessAmount
                    nextRow[glassIndex + 1] += excessAmount

            currentRow = nextRow

        return min(1.0, currentRow[query_glass])
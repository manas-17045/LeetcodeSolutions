# Leetcode 3418: Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/
# Solved on 16th of August, 2025
class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        """
        Calculates the maximum amount of money a robot can earn by traversing a grid of coins.

        Args:
            coins: A 2D list of integers representing the grid of coins.
        Returns:
            The maximum amount of money the robot can earn as an integer.
        """
        numRows = len(coins)
        numCols = len(coins[0])

        negInf = float('-inf')
        previousRowDp = [[negInf] * 3 for _ in range(numCols)]

        # Initialize for thr first cel (0, 0)
        cellValue = coins[0][0]
        if cellValue >= 0:
            previousRowDp[0][0] = cellValue
        else:
            previousRowDp[0][0] = cellValue
            previousRowDp[0][1] = 0

        # Initialize the rest of the first row
        for j in range(1, numCols):
            cellValue = coins[0][j]
            fromLeft = previousRowDp[j - 1]
            for k in range(3):
                if cellValue >= 0:
                    if fromLeft[k] != negInf:
                        previousRowDp[j][k] = fromLeft[k] + cellValue
                else:
                    profitA = negInf
                    if fromLeft[k] != negInf:
                        profitA = fromLeft[k] + cellValue

                    profitB = negInf
                    if k > 0 and fromLeft[k - 1] != negInf:
                        profitB = fromLeft[k - 1]

                    previousRowDp[j][k] = max(profitA, profitB)

        # Fill DP table for the remaining rows
        for i in range(1, numRows):
            currentRowDp = [[negInf] * 3 for _ in range(numCols)]
            for j in range(numCols):
                cellValue = coins[i][j]

                fromAbove = previousRowDp[j]
                fromLeft = [negInf] * 3 if j == 0 else currentRowDp[j - 1]

                for k in range(3):
                    maxPrevK = max(fromAbove[k], fromLeft[k])

                    maxPrevKMinusOne = negInf
                    if k > 0:
                        maxPrevKMinusOne = max(fromAbove[k - 1], fromLeft[k - 1])

                    if cellValue >= 0:
                        if maxPrevK != negInf:
                            currentRowDp[j][k] = maxPrevK + cellValue
                    else:
                        # Robber
                        profitA = negInf
                        if maxPrevK != negInf:
                            currentRowDp[j][k] = maxPrevK + cellValue

                        profitB = negInf
                        if k > 0 and maxPrevKMinusOne != negInf:
                            profitB = maxPrevKMinusOne

                        currentRowDp[j][k] = max(profitA, profitB)

            previousRowDp = currentRowDp

        finalProfits = previousRowDp[numCols - 1]
        result = max(finalProfits)

        return int(result)
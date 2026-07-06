# Leetcode 1301: Number of Paths with Max Score
# https://leetcode.com/problems/number-of-paths-with-max-score/
# Solved on 5th of July, 2026
class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        """
        Calculates the maximum score and the number of paths to achieve it in a grid.

        Args:
            board: The grid represented as an array of strings.

        Returns:
            An array containing the maximum score and the number of paths.
        """
        boardSize = len(board)
        modValue = 10**9 + 7

        prevMax = [-1] * (boardSize + 1)
        prevWays = [0] * (boardSize + 1)

        for rowIdx in range(boardSize - 1, -1, -1):
            currMax = [-1] * (boardSize + 1)
            currWays = [0] * (boardSize + 1)

            for colIdx in range(boardSize - 1, -1, -1):
                cellChar = board[rowIdx][colIdx]
                
                if cellChar == 'X':
                    continue
                    
                if rowIdx == boardSize - 1 and colIdx == boardSize - 1:
                    currMax[colIdx] = 0
                    currWays[colIdx] = 1
                    continue
                    
                maxSumValue = max(prevMax[colIdx], currMax[colIdx + 1], prevMax[colIdx + 1])
                
                if maxSumValue != -1:
                    waysCount = 0
                    if prevMax[colIdx] == maxSumValue:
                        waysCount = (waysCount + prevWays[colIdx]) % modValue
                    if currMax[colIdx + 1] == maxSumValue:
                        waysCount = (waysCount + currWays[colIdx + 1]) % modValue
                    if prevMax[colIdx + 1] == maxSumValue:
                        waysCount = (waysCount + prevWays[colIdx + 1]) % modValue
                        
                    addValue = 0
                    if cellChar not in ('E', 'S'):
                        addValue = int(cellChar)
                    
                    currMax[colIdx] = maxSumValue + addValue
                    currWays[colIdx] = waysCount

            prevMax = currMax
            prevWays = currWays

        return [prevMax[0], prevWays[0]] if prevMax[0] != -1 else [0, 0]
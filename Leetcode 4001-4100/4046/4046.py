# Leetcode 4046: Minimum Cost Path With At Most K Turns
# https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/
# Solved on 8th of October, 2026
import heapq


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        """
        Calculates the minimum cost path to reach the bottom-right cell with at most k turns.
        
        Args:
            grid (list[list[int]]): A 2D array representing the cost of visiting each cell.
            k (int): The maximum number of allowed turns.
            
        Returns:
            int: The minimum cost to reach the destination, or -1 if no such path exists.
        """
        rowCount = len(grid)
        colCount = len(grid[0])
        
        if rowCount == 1 and colCount == 1:
            return grid[0][0]
            
        minTurns = [[[k + 1 for _ in range(4)] for _ in range(colCount)] for _ in range(rowCount)]
        minTurnsStart = k + 1
        
        dirRow = [0, 1, 0, -1]
        dirCol = [1, 0, -1, 0]
        
        priorityQueue = []
        heapq.heappush(priorityQueue, (grid[0][0], 0, 0, -1, 0))
        
        while priorityQueue:
            currCost, currRow, currCol, currDir, currTurns = heapq.heappop(priorityQueue)
            
            if currRow == rowCount - 1 and currCol == colCount - 1:
                return currCost
                
            if currDir == -1:
                if currTurns >= minTurnsStart:
                    continue
                minTurnsStart = currTurns
            else:
                if currTurns >= minTurns[currRow][currCol][currDir]:
                    continue
                minTurns[currRow][currCol][currDir] = currTurns
                
            for nextDir in range(4):
                nextRow = currRow + dirRow[nextDir]
                nextCol = currCol + dirCol[nextDir]
                
                if 0 <= nextRow < rowCount and 0 <= nextCol < colCount:
                    nextTurns = currTurns
                    
                    if currDir != -1 and currDir != nextDir:
                        nextTurns += 1
                        
                    if nextTurns <= k:
                        nextCost = currCost + grid[nextRow][nextCol]
                        heapq.heappush(priorityQueue, (nextCost, nextRow, nextCol, nextDir, nextTurns))
                        
        return -1
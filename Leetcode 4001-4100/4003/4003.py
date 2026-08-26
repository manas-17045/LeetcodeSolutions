# Leetcode 4003: Minimum Cost Path with Alternating Directions III
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/
# Solved on 26th of August, 2026
import heapq


class Solution:
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        """
        Calculates the minimum total cost required to reach the bottom-right cell of a grid.
        
        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.
            penalty (List[List[int]]): A 2D array representing the penalty for violating parity rules or waiting.
            
        Returns:
            int: The minimum total cost to reach the destination cell.
        """
        dist = [float('inf')] * (m * n * 2)
        dist[1] = 1

        minHeap = [(1, 0, 0, 1)]

        while minHeap:
            currCost, currRow, currCol, currParity = heapq.heappop(minHeap)

            if currRow == m - 1 and currCol == n - 1:
                return currCost

            stateIdx = (currRow * n + currCol) * 2 + currParity

            if currCost > dist[stateIdx]:
                continue

            nextParity = 1 - currParity
            waitCost = currCost + penalty[currRow][currCol]
            waitIdx = (currRow * n + currCol) * 2 + nextParity

            if waitCost < dist[waitIdx]:
                dist[waitIdx] = waitCost
                heapq.heappush(minHeap, (waitCost, currRow, currCol, nextParity))

            for dirRow, dirCol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nextRow = currRow + dirRow
                nextCol = currCol + dirCol

                if 0 <= nextRow < m and 0 <= nextCol < n:
                    destCost = (nextRow + 1) * (nextCol + 1)
                    isValid = (currParity == 1 and (dirRow == 1 or dirCol == 1)) or (currParity == 0 and (dirRow == -1 or dirCol == -1))
                    extraCost = 0 if isValid else penalty[currRow][currCol]

                    nextCost = currCost + destCost + extraCost
                    nextIdx = (nextRow * n + nextCol) * 2 + nextParity

                    if nextCost < dist[nextIdx]:
                        dist[nextIdx] = nextCost
                        heapq.heappush(minHeap, (nextCost, nextRow, nextCol, nextParity))

        return -1
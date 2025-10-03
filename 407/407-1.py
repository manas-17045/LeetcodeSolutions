# Leetcode 407: Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/
# Resolved on 3rd of October, 2025
import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        """
        Calculates the amount of water that can be trapped within a 2D height map.

        This problem is similar to "Trapping Rain Water" but in 2D. It uses a
        min-heap to simulate water filling from the boundaries inwards.

        Args:
            heightMap (list[list[int]]): A 2D list of integers representing the height map.

        Returns:
            int: The total amount of water trapped.
        """
        if not heightMap or not heightMap[0]:
            return 0

        numRows = len(heightMap)
        numCols = len(heightMap[0])

        if numRows < 3 or numCols < 3:
            return 0

        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        minHeap = []

        for r in range(numRows):
            for c in range(numCols):
                if r == 0 or c == 0 or r == numRows - 1 or c == numCols - 1:
                    heapq.heappush(minHeap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        totalWater = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minHeap:
            height, r, c = heapq.heappop(minHeap)

            for dr, dc in directions:
                newRow, newCol = r + dr, c + dc

                if 0 <= newRow < numRows and 0 <= newCol < numCols and not visited[newRow][newCol]:
                    visited[newRow][newCol] = True
                    neighborHeight = heightMap[newRow][newCol]

                    waterToAdd = max(0, height - neighborHeight)
                    totalWater += waterToAdd

                    pushHeight = max(height, neighborHeight)
                    heapq.heappush(minHeap, (pushHeight, newRow, newCol))

        return totalWater
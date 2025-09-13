# Leetcode 2146: K Highest Ranked Items Within a Price Range
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/
# Solved on 13th of September, 2025
import collections


class Solution:
    def hoghestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], k: int) -> list[list[int]]:
        """
        Finds the k highest-ranked items within a given price range, starting from a specified cell.

        Args:
            grid (list[list[int]]): The grid representing the shopping area, where each cell contains an item's price or 0 if it's a wall.
            pricing (list[int]): A list containing two integers [priceLow, priceHigh] defining the acceptable price range.
            start (list[int]): A list containing two integers [startRow, startCol] representing the starting coordinates.
            k (int): The number of highest-ranked items to return.

        Returns:
            list[list[int]]: A list of lists, where each inner list [row, col] represents the coordinates of a found item, sorted by rank.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        priceLow, priceHigh = pricing
        startRow, startCol = start

        queue = collections.deque([(startRow, startCol, 0)])
        visited = {(startRow, startCol)}

        foundItems = []

        while queue:
            currentRow, currentCol, currentDist = queue.popleft()

            currentPrice = grid[currentRow][currentCol]

            if currentPrice > 1 and priceLow <= currentPrice <= priceHigh:
                foundItems.append((currentDist, currentPrice, currentRow, currentCol))

            for rowOffset, colOffset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nextRow = currentRow + rowOffset
                nextCol = currentCol + colOffset

                if 0 <= nextRow < numRows and 0 <= nextCol < numCols and (nextRow, nextCol) not in visited:

                    visited.add((nextRow, nextCol))
                    queue.append((nextRow, nextCol, currentDist + 1))

        foundItems.sort()

        resultList = []

        limit = min(k, len(foundItems))
        for i in range(limit):
            itemData = foundItems[i]
            resultList.append([itemData[2], itemData[3]])

        return resultList
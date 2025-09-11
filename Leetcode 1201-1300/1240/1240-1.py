# Leetcode 1240: Tiling a Rectangle with ethe Fewest Squares
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
# Solved on 11th of September, 2025
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        Given a rectangle of size n x m, find the minimum number of squares that can tile the rectangle.

        Args:
            n (int): The height of the rectangle.
            m (int): The width of the rectangle.

        Returns:
            int: The minimum number of squares required to tile the rectangle.
        """

        if n > m:
            n, m = m, n

        if n == m:
            return 1

        self.minSquares = m * n
        self.memo = {}

        initialSkyline = tuple([0] * n)
        self.backtrack(initialSkyline, 0, n, m)
        return self.minSquares

    def backtrack(self, skyline, count, height, width):
        if count >= self.minSquares:
            return

        if skyline in self.memo and self.memo[skyline] <= count:
            return
        self.memo[skyline] = count

        minFilledWidth = width
        firstUnfilledRow = -1
        for i in range(height):
            if skyline[i] < minFilledWidth:
                minFilledWidth = skyline[i]
                firstUnfilledRow = i

        if minFilledWidth == width:
            self.minSquares = min(self.minSquares, count)
            return

        endRow = firstUnfilledRow
        while endRow + 1 < height and skyline[endRow + 1] == minFilledWidth:
            endRow += 1

        gapHeight = endRow - firstUnfilledRow + 1

        maxSize = min(gapHeight, (width - minFilledWidth))

        for size in range(maxSize, 0, -1):
            newSkyline = list(skyline)
            for i in range(firstUnfilledRow, firstUnfilledRow + size):
                newSkyline[i] = minFilledWidth + size

            self.backtrack(tuple(newSkyline), count + 1, height, width)
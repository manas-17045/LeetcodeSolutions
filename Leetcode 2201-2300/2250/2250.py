# Leetcode 2250: Count Number of Rectangles Containing Each Point
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/
# Solved on 8th of November, 2025
import bisect


class Solution:
    def countRectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
        """
        Counts the number of rectangles that contain each given point.

        :param rectangles: A list of rectangles, where each rectangle is represented as [l, h] (length, height).
        :param points: A list of points, where each point is represented as [x, y] (x-coordinate, y-coordinate).
        :return: A list of integers, where each element is the count of rectangles containing the corresponding point.
        """
        rectsByHeight = [[] for _ in range(101)]

        for l, h in rectangles:
            rectsByHeight[h].append(l)

        for h in range(101):
            rectsByHeight[h].sort()

        ans = []

        for px, py in points:
            currentCount = 0
            for h in range(py, 101):
                sortedLengths = rectsByHeight[h]
                index = bisect.bisect_left(sortedLengths, px)
                countAtHeight = len(sortedLengths) - index
                currentCount += countAtHeight

            ans.append(currentCount)

        return ans
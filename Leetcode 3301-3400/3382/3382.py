# Leetcode 3382: Maximum Area Rectangle With Point Constraints II
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/
# Solved on 29th of October, 2025
import collections


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [-1] * (4 * self.size)

    def _update(self, treeIndex, start, end, index, value):
        if start == end:
            self.tree[treeIndex] = value
            return

        mid = start + (end - start) // 2
        leftSubtree = 2 * treeIndex + 1
        rightSubtree = 2 * treeIndex + 2

        if index <= mid:
            self._update(leftSubtree, start, mid, index, value)
        else:
            self._update(rightSubtree, mid + 1, end, index, value)

        self.tree[treeIndex] = max(self.tree[leftSubtree], self.tree[rightSubtree])

    def update(self, index, value):
        self._update(0, 0, self.size - 1, index, value)

    def _query(self, treeIndex, start, end, left, right):
        if left > right:
            return -1

        if left <= start and end <= right:
            return self.tree[treeIndex]

        if end < left or start > right:
            return -1

        mid = start + (end - start) // 2
        leftSubtree = 2 * treeIndex + 1
        rightSubtree = 2 * treeIndex + 2

        leftResult = self._query(leftSubtree, start, mid, left, right)
        rightResult = self._query(rightSubtree, mid + 1, end, left, right)

        return max(leftResult, rightResult)

    def query(self, left, right):
        return self._query(0, 0, self.size - 1, left, right)

class Solution:
    def maxRectangleArea(self, xCoord: list[int], yCoord: list[int]) -> int:
        """
        Calculates the maximum area of a rectangle formed by a subset of given points,
        such that the rectangle contains no other points in its interior.
        :param xCoord: A list of x-coordinates of the points.
        :param yCoord: A list of y-coordinates of the points.
        :return: The maximum area of such a rectangle, or -1 if no such rectangle can be formed.
        """
        if not xCoord:
            return -1

        uniqueYs = sorted(list(set(yCoord)))
        yToIndex = {y: i for i, y in enumerate(uniqueYs)}

        pointsByX = collections.defaultdict(list)
        for x, y in zip(xCoord, yCoord):
            pointsByX[x].append(y)

        segmentTree = SegmentTree(len(uniqueYs))
        yToX = {}
        maxArea = -1

        sortedXs = sorted(pointsByX.keys())

        for x in sortedXs:
            ysAtX = sorted(pointsByX[x])
            for i in range(len(ysAtX) - 1):
                yBottom = ysAtX[i]
                yTop = ysAtX[i + 1]

                xLeftBottom = yToX.get(yBottom, -1)
                xLeftTop = yToX.get(yTop, -1)

                if xLeftBottom != -1 and xLeftBottom == xLeftTop:
                    xLeft = xLeftBottom
                    yBottomIndex = yToIndex[yBottom]
                    yTopIndex = yToIndex[yTop]

                    maxXInside = segmentTree.query(yBottomIndex + 1, yTopIndex - 1)

                    if xLeft > maxXInside:
                        area = (x - xLeft) * (yTop - yBottom)
                        if area > maxArea:
                            maxArea = area

            for y in ysAtX:
                yToX[y] = x
                segmentTree.update(yToIndex[y], x)

        return maxArea
# Leetcode 3235: Check if the Rectangle Corner Is Reachable
# https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/
# Solved on 13th of December, 2025
import math


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: list[list[int]]) -> bool:
        """
        Determines if the bottom-left corner (0,0) of a rectangle can reach the top-right corner (xCorner, yCorner)
        without intersecting any of the given circles.

        The movement is restricted to within the rectangle boundaries.

        Args:
            xCorner (int): The x-coordinate of the top-right corner of the rectangle.
            yCorner (int): The y-coordinate of the top-right corner of the rectangle.
            circles (list[list[int]]): A list of circles, where each circle is represented as [cx, cy, r],
                                       with (cx, cy) being the center and r being the radius.

        Returns:
            bool: True if the bottom-left corner can reach the top-right corner, False otherwise.
        """
        for x, y, r in circles:
            if x ** 2 + y ** 2 <= r ** 2:
                return False
            if (x - xCorner) ** 2 + (y - yCorner) ** 2 <= r ** 2:
                return False

        n = len(circles)
        parent = list(range(n + 4))
        top, bottom, left, right = n, n + 1, n + 2, n + 3

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parent[rootJ] = rootI

        def inRect(x, y):
            return 0 <= x <= xCorner and 0 <= y <= yCorner

        def segmentIntersectsRect(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if inRect(x1, y1) or inRect(x2, y2):
                return True

            dx, dy = x2 - x1, y2 - y1
            if dx == 0 and dy == 0:
                return False

            ts = []
            if dx != 0:
                ts.append((0 - x1) / dx)
                ts.append((xCorner - x1) / dx)
            if dy != 0:
                ts.append((0 - y1) / dy)
                ts.append((yCorner - y1) / dy)

            for t in ts:
                if 0 <= t <= 1:
                    ix = x1 + t * dx
                    iy = y1 + t * dy
                    if -1e-5 <= ix <= xCorner + 1e-5 and -1e-5 <= iy <= yCorner + 1e-5:
                        return True

            return False

        for i, (cx, cy, r) in enumerate(circles):
            if abs(cy - yCorner) <= r and (
                    0 <= cx <= xCorner or (cx < 0 and cx ** 2 + (cy - yCorner) ** 2 <= r ** 2) or (
                    cx > xCorner and (cx - xCorner) ** 2 + (cy - yCorner) ** 2 <= r ** 2)):
                union(i, top)
            if abs(cy) <= r and (0 <= cx <= xCorner or (cx < 0 and cx ** 2 + cy ** 2 <= r ** 2) or (
                    cx > xCorner and (cx - xCorner) ** 2 + cy ** 2 <= r ** 2)):
                union(i, bottom)
            if abs(cx) <= r and (0 <= cy <= yCorner or (cy < 0 and cx ** 2 + cy ** 2 <= r ** 2) or (
                    cy > yCorner and cx ** 2 + (cy - yCorner) ** 2 <= r ** 2)):
                union(i, left)
            if abs(cx - xCorner) <= r and (
                    0 <= cy <= yCorner or (cy < 0 and (cx - xCorner) ** 2 + cy ** 2 <= r ** 2) or (
                    cy > yCorner and (cx - xCorner) ** 2 + (cy - yCorner) ** 2 <= r ** 2)):
                union(i, right)

        for i in range(n):
            for j in range(i + 1, n):
                xi, yi, ri = circles[i]
                xj, yj, rj = circles[j]
                d2 = (xi - xj) ** 2 + (yi - yj) ** 2
                rSum = ri + rj

                if d2 > rSum ** 2:
                    continue

                connected = False

                if inRect(xi, yi) or inRect(xj, yj):
                    connected = True
                else:
                    d = math.sqrt(d2)
                    if d == 0:
                        if abs(ri - rj) >= 0:
                            connected = True
                    else:
                        a = (ri ** 2 - rj ** 2 + d2) / (2 * d)
                        h = math.sqrt(max(0, ri ** 2 - a ** 2))
                        x2 = xi + a * (xj - xi) / d
                        y2 = yi + a * (yj - yi) / d

                        x31 = x2 + h * (yj - yi) / d
                        y31 = y2 - h * (xj - xi) / d
                        x32 = x2 - h * (yj - yi) / d
                        y32 = y2 + h * (xj - xi) / d

                        p1 = (x31, y31)
                        p2 = (x32, y32)

                        if segmentIntersectsRect(p1, p2):
                            connected = True

                if connected:
                    union(i, j)

        if find(top) == find(bottom) or find(left) == find(right) or \
                find(top) == find(right) or find(bottom) == find(left):
            return False

        return True
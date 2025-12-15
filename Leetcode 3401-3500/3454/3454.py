# Leetcode 3454: Separate Squares II
# https://leetcode.com/problems/separate-squares-ii/
# Solved on 15th of December, 2025
class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        """
        Calculates the y-coordinate that separates the total area covered by a set of squares into two equal halves.

        Args:
            squares: A list of lists, where each inner list represents a square [x, y, side_length].

        Returns:
            A float representing the y-coordinate that bisects the total covered area.
        """
        n = len(squares)
        events = []
        xCoordsSet = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xCoordsSet.add(x)
            xCoordsSet.add(x + l)

        events.sort(key=lambda e: e[0])
        xCoords = sorted(list(xCoordsSet))
        xMap = {val: i for i, val in enumerate(xCoords)}
        m = len(xCoords)

        count = [0] * (4 * m)
        length = [0.0] * (4 * m)

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                count[node] += val
            else:
                mid = (start + end) // 2
                update(2 * node + 1, start, mid, l, r, val)
                update(2 * node + 2, mid + 1, end, l, r, val)

            if count[node] > 0:
                length[node] = xCoords[end + 1] - xCoords[start]
            elif start != end:
                length[node] = length[2 * node + 1] + length[2 * node + 2]
            else:
                length[node] = 0.0

        totalArea = 0.0
        prevY = events[0][0]
        history = []

        for y, type, x1, x2 in events:
            if y > prevY:
                currentLen = length[0]
                totalArea += currentLen * (y - prevY)
                history.append((y, totalArea))
                prevY = y

            lIdx = xMap[x1]
            rIdx = xMap[x2]

            if lIdx < rIdx:
                update(0, 0, m - 2, lIdx, rIdx - 1, type)

        target = totalArea / 2.0
        currentTotal = 0.0
        prevY = events[0][0]

        for y, area in history:
            if area >= target:
                dy = y - prevY
                da = area - currentTotal
                return prevY + (target - currentTotal) * dy / da
            currentTotal = area
            prevY = y

        return prevY
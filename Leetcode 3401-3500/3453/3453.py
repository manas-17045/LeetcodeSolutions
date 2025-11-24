# Leetcode 3453: Separate Squares I
# https://leetcode.com/problems/separate-squares-i/
# Solved on 24th of November, 2025
class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        """
        Calculates the y-coordinate of a horizontal line that separates the total area
        of a set of squares into two equal halves.

        Args:
            squares: A list of lists, where each inner list represents a square
                     in the format [x, y, side_length].

        Returns:
            A float representing the y-coordinate of the separating line.
        """
        totalArea = 0
        events = []
        for _, y, l in squares:
            totalArea += l * l
            events.append((y, l))
            events.append((y + l, -l))

        events.sort()

        targetArea = totalArea / 2.0
        currentArea = 0
        currentWidth = 0
        prevY = events[0][0]

        for y, widthChange in events:
            height = y - prevY
            segmentArea = height * currentWidth

            if currentArea + segmentArea >= targetArea:
                return prevY + (targetArea - currentArea) / currentWidth

            currentArea += segmentArea
            currentWidth += widthChange
            prevY = y

        return float(prevY)